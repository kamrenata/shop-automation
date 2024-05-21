import os
import subprocess
import zipfile
import platform

import requests
from tqdm import tqdm
from colorama import Fore
import pathlib

# TODO: Wrap to the class
# TODO: Add reinstall method to handle unexpected errors
# TODO: Test on win (looks no one uses it, but nice to have)
# TODO: Exclude local config from git and fetch platform

# TODO: Avoid hardcode. Use smart path joining
paths = {
    "mac-arm64": {
        "chrome": "chrome/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
        "chromedriver": "chromedriver/chromedriver-mac-arm64/chromedriver",
    },
    # TODO: Check if it works
    "mac-x64": {
        "chrome": "chrome/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
        "chromedriver": "chromedriver/chromedriver-mac-x64/chromedriver",
    },
    "linux64": {
        "chrome": "chrome/chrome-linux64/chrome",
        "chromedriver": "chromedriver/chromedriver-linux64/chromedriver",
    },
    "win64": {
        "chrome": "chrome/chrome-win64/chrome.exe",
        "chromedriver": "chromedriver/chromedriver-win64/chromedriver.exe",
    },
}


def get_platform(pf=None):
    """Gets platform name based on current system
    Returns: (str) - platform name
    """
    if pf:
        return pf
    system_type = platform.system()

    if system_type == "Darwin":
        if platform.machine() == "arm64":
            return "mac-arm64"
        elif platform.machine() == "x86_64":
            # TODO: Modify to the correct platform code
            return "mac-arm64"
    elif system_type == "Linux":
        return "linux64"
    elif system_type == "Windows":
        if "32bit" in platform.architecture():
            return "win32"
        if "64bit" in platform.architecture():
            return "win64"
    else:
        raise ValueError("Unsupported operating system")


ROOT = str(pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent)
ZIP_DIR = os.path.join(ROOT, "temp.zip")
CHROME_DIR = os.path.join(ROOT, "chrome")
CHROMEDRIVER_DIR = os.path.join(ROOT, "chromedriver")


def get_stable_chrome(platform, only_driver=False) -> list:
    """
    Retrieves stable chrome/driver release from official json API
    Args:
        platform: os
        only_driver: Flag to fetch only chromedriver

    Returns: (list) - chrome, chromedriver

    """
    # URL for the last-known-good-versions JSON
    json_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"

    try:
        # Fetch JSON data from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse JSON data
        data = response.json()["channels"]["Stable"]["downloads"]
        result = []

        if not only_driver:
            for p in data["chrome"]:
                if platform in p["platform"]:
                    result.append(p["url"])

        for p in data["chromedriver"]:
            if platform in p["platform"]:
                result.append(p["url"])

        if result:
            return result

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


def is_latest_chrome_installed():
    """Checks if latest stable versions of Chrome / chromedriver are installed"""
    if os.path.exists(CHROME_DIR) and os.path.exists(CHROMEDRIVER_DIR):
        # TODO: Parse temp file to get version of chrome (Merge slack-reports at first)
        ...


def download_chrome(urls: list, only_driver=False):
    for url in urls:
        response = requests.get(url, stream=True)

        with tqdm(
            total=int(response.headers.get("content-length", 0)),
            desc=f"{Fore.GREEN}Installing {'Chrome Driver' if 'driver' in url else 'Chrome For Testing'}",
            unit="iB",
            unit_scale=True,
            dynamic_ncols=True,
        ) as progress_bar:

            with open(ZIP_DIR, "wb") as file:
                for data in response.iter_content(1024):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.set_postfix_str(f"{progress_bar.desc} is Completed!")

        extract_dir = CHROMEDRIVER_DIR if "driver" in url else CHROME_DIR
        os.makedirs(extract_dir, exist_ok=True)

        with zipfile.ZipFile(ZIP_DIR, "r") as zip_ref:
            zip_ref.extractall(extract_dir)

        os.remove(ZIP_DIR)

        try:
            if not only_driver:
                subprocess.run(["chmod", "-R", "777", CHROME_DIR], check=True)
            subprocess.run(["chmod", "-R", "777", CHROMEDRIVER_DIR], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")


def get_chrome_paths(pf=get_platform(), only_driver=False):
    """Gets chrome and chromedriver paths based on current system
    Returns: (str, str) - chrome path, chromedriver path
    """

    # Install chrome and chromedriver if not installed
    if only_driver:
        if not os.path.exists(CHROMEDRIVER_DIR):
            download_chrome(get_stable_chrome(get_platform(pf), only_driver), only_driver)
        if os.path.exists(CHROMEDRIVER_DIR):
            return paths[get_platform(pf)].get("chromedriver")
        else:
            raise FileNotFoundError("ChromeDriver is not installed")
    if not (os.path.exists(CHROME_DIR) and os.path.exists(CHROMEDRIVER_DIR)):
        download_chrome(get_stable_chrome(get_platform(pf)))
    if os.path.exists(CHROME_DIR) and os.path.exists(CHROMEDRIVER_DIR):
        return paths[pf].get("chrome"), paths[pf].get("chromedriver")
    else:
        raise FileNotFoundError("ChromeDriver is not installed")

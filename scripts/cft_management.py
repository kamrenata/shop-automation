import os
import subprocess
import zipfile

import requests
from tqdm import tqdm
from colorama import Fore
import pathlib

# TODO: Wrap to the class
# TODO: Add reinstall method to handle unexpected errors
# TODO: Dispatch paths depending on system
# TODO: Test on win (looks no one uses it, but nice to have)
# TODO: Exclude local config from git and fetch platform


system = {
    "mac_m1": "mac-arm64",
    "mac": "mac-x64",
    "linux": "linux64",
    "win64": "win64",
}

ROOT = str(pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent)
ZIP_DIR = os.path.join(ROOT, 'temp.zip')
CHROME_DIR = os.path.join(ROOT, 'chrome')
CHROMEDRIVER_DIR = os.path.join(ROOT, 'chromedriver')


def get_stable_chrome(platform) -> list:
    """
    Retrieves stable chrome/driver release from official json API
    Args:
        platform: os

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


def download_chrome(urls: list):
    for url in urls:
        response = requests.get(url, stream=True)

        with tqdm(total=int(response.headers.get('content-length', 0)),
                  desc=f"{Fore.GREEN}Installing {'Chrome Driver' if 'driver' in url else 'Chrome For Testing'}",
                  unit='iB',
                  unit_scale=True,
                  dynamic_ncols=True
                  ) as progress_bar:

            with open(ZIP_DIR, 'wb') as file:
                for data in response.iter_content(1024):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.set_postfix_str(f"{progress_bar.desc} is Completed!")

        extract_dir = CHROMEDRIVER_DIR if "driver" in url else CHROME_DIR
        os.makedirs(extract_dir, exist_ok=True)

        with zipfile.ZipFile(ZIP_DIR, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        os.remove(ZIP_DIR)

    try:
        subprocess.run(['chmod', '-R', '777', CHROME_DIR], check=True)
        subprocess.run(['chmod', '-R', '777', CHROMEDRIVER_DIR], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# if not (os.path.exists(CHROME_DIR) and os.path.exists(CHROMEDRIVER_DIR)) and os.getenv("cft", False):
    # TODO: Check is latest version is installed and then pass
# a = get_stable_chrome("mac-arm64")
# download_chrome(a)

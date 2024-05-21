import os
import pytest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from scripts.cft_management import ROOT, get_chrome_paths


# options.binary_location = os.path.join(
#     # TODO: Rework path based on system
#     ROOT, 'chrome/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing')
#
# driver = webdriver.Chrome(
#             options=options,
#             # TODO: Rework path based on system
#             executable_path=os.path.join(ROOT, "chromedriver/chromedriver-mac-arm64/chromedriver")
#             )


@pytest.fixture(autouse=True)
def driver():
    """Create chrome driver for Selenium"""
    chrome_path, chromedriver_path = get_chrome_paths()
    options = ChromeOptions()
    options.binary_location = str(
        os.path.join(
            ROOT,
            chrome_path
        )
    )

    driver = Chrome(
        options=options,
        service=Service(
            executable_path=str(
                os.path.join(ROOT, chromedriver_path)
            )
        ),
    )
    yield driver
    driver.quit()

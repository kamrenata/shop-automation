import os
import pytest

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from scripts.cft_management import ROOT


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
    options = ChromeOptions()
    # options.binary_location = "chrome/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome
    # for Testing"
    options.binary_location = str(
        os.path.join(
            ROOT,
            "chrome/chrome-mac-arm64/Google Chrome for "
            "Testing.app/Contents/MacOS/Google Chrome for Testing",
        )
    )

    driver = Chrome(
        options=options,
        # service=Service(executable_path="chromedriver/chromedriver-mac-arm64/chromedriver"))
        service=Service(
            executable_path=str(
                os.path.join(ROOT, "chromedriver/chromedriver-mac-arm64/chromedriver")
            )
        ),
    )
    # (executable_path=str(os.path.join(os.getcwdu(), "chromedriver/chromedriver-mac-arm64/chromedriver"))))
    yield driver
    driver.quit()

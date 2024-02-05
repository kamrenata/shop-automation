from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def find_by_id(driver, locator) -> WebElement:
    return driver.find_element(By.ID, locator)

def find_by_class(driver, locator) -> WebElement:
    return driver.find_element(By.CLASS_NAME, locator)


class BasePage:
    """Class which reflects locators on the main page"""
    logo = "logo"
    start_button = "btn-download"
    explore_button = "btn-explore"
    url = "https://demo.prestashop.com/#/en/front"



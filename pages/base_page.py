from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExpectedConditions:
    pass


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def open_url(self, url):
        self.driver.get(url)

    def wait_element_absent(self, locator, timeout=10):
        WebDriverWait(
            driver=self.driver, timeout=timeout
        ).until(EC.invisibility_of_element(self.find_element(locator)))

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class ExpectedConditions:
    pass


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.fake: Faker = Faker()

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def open_url(self, url):
        self.driver.get(url)

    def wait_element_absent(self, locator, timeout=10):
        WebDriverWait(driver=self.driver, timeout=timeout).until(
            EC.invisibility_of_element(self.find_element(locator))
        )

    def wait_element_is_present(self, locator: tuple, timeout=10):
        WebDriverWait(driver=self.driver, timeout=timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_element_by_unique_text(self, text):
        self.find_element((By.XPATH, f"//text()[. = '{text}']"))

    def switch_to_frame(self, frame_id: str):
        self.driver.switch_to.frame(self.find_element((By.ID, frame_id)))

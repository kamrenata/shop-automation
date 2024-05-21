from selenium.webdriver.common.by import By

from .base_page import BasePage


class SignInPage(BasePage):
    """Class which reflects locators on the sign in page"""

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://demo.prestashop.com/#/en/front"

    no_account_button = (By.CLASS_NAME, "no-account")
    female_gender_radio_button = (By.ID, "field-id_gender-2")
    name_field = (By.ID, "field-firstname")
    lastname_field = (By.ID, "field-lastname")
    email_field = (By.ID, "field-email")
    password_field = (By.ID, "field-password")
    privacy_policy_checkbox = (By.CSS_SELECTOR, 'input[name="psgdpr"]')
    data_privacy_checkbox = (By.CSS_SELECTOR, 'input[name="customer_privacy"]')
    submit_button = (By.CLASS_NAME, "form-control-submit")
    log_in_text = (By.XPATH, '//h1[contains(text(), "Log in")]')
    new_account = (By.CSS_SELECTOR, ".no-account > a")
    sign_out_button = (By.CSS_SELECTOR, ".user-info > a")

    def submit_form_with_valid_fields(self):
        self.find_element(self.female_gender_radio_button).click()
        self.find_element(self.name_field).send_keys(self.fake.first_name())
        self.find_element(self.lastname_field).send_keys(self.fake.last_name())
        self.find_element(self.email_field).send_keys(self.fake.email())
        self.find_element(self.password_field).send_keys(
            self.fake.pystr(min_chars=8, max_chars=10)
        )
        self.find_element(self.privacy_policy_checkbox).click()
        self.find_element(self.data_privacy_checkbox).click()
        self.find_element(self.submit_button).click()

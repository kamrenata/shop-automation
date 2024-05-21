from pages.main_page import *
from pages.sign_in_page import *
from time import sleep


def test_register_user(driver):
    """
    Wait till loader is disappeared+
    Sign in form is present+
    Login page is present+
    Click No account Create one here
    Fill all required fields
    Save
    """
    page = MainPage(driver)
    page.open_url(page.url)
    page.wait_element_absent(page.loader, 15)
    sleep(1)
    page.switch_to_frame("frame-live")
    page.find_element(page.sign_in_button).click()
    sign_in_page = SignInPage(driver)
    sign_in_page.wait_element_is_present(sign_in_page.log_in_text)
    sign_in_page.find_element(sign_in_page.new_account).click()
    sign_in_page.submit_form_with_valid_fields()
    sleep(5)
    sign_in_page.find_element(sign_in_page.sign_out_button)

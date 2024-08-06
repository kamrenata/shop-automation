# from selenium.webdriver.common.by import By

from .base_page import BasePage, By


class MainPage(BasePage):
    """Class which reflects locators on the main page"""

    def __init__(self, driver):
        super().__init__(driver)

    url = "https://demo.prestashop.com/#/en/front"

    logo = (By.ID, "logo")
    start_button = (By.CLASS_NAME, "btn-download")
    explore_button = (By.CLASS_NAME, "btn-explore")
    loader = (By.ID, "loadingMessage")
    sign_out_button = (By.CLASS_NAME, "logout hidden-sm-down")
    sign_in_button = (By.CLASS_NAME, "user-info")
    clothes_button = (By.ID, "category-3")
    men_clothes_button = (By.ID, "category-4")
    women_clothes_button = (By.ID, "category-5")
    accessories_button = (By.ID, "category-6")
    stationery_button = (By.ID, "category-7")
    home_accessories_button = (By.ID, "category-8")
    art_button = (By.ID, "category-9")
    search_field = (By.ID, "search_widget")
    language_drop_down_list = (By.CLASS_NAME, "expand-more")



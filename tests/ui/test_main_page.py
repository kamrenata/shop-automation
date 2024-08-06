from pages.main_page import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from tests.ui.test_base import TestBase


class TestMainPage:
    def test_logo_is_present(self, driver):
        """To verify that logo is visible"""
        page = MainPage(driver)
        page.open_url(page.url)
        sleep(3)
        page.find_element(page.logo)

    def test_start_button_is_visible(self, driver):
        """To verify that "Start Now" button is visible"""
        page = MainPage(driver)
        page.open_url(page.url)
        sleep(3)
        page.find_element(page.start_button)

    def test_explore_button_is_visible(self, driver):
        """To verify that "Explore Back Office button" is visible"""
        page = MainPage(driver)
        page.open_url(page.url)
        sleep(3)
        page.find_element(page.explore_button)

    def test_second_loader_is_absent(self, driver):
        page = MainPage(driver)
        page.open_url(page.url)
        page.wait_element_absent(page.loader)

    def test_navigate_to_mens_clothes(self, driver):
        page = MainPage(driver)
        page.open_url(page.url)
        navigate = ActionChains(driver)
        navigate.move_to_element(page.clothes_button)
        page.find_element(page.men_clothes_button).click()

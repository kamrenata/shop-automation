from pages.main_page import *
from time import sleep


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

    def test_first_loader_is_absent(self, driver):
        ...

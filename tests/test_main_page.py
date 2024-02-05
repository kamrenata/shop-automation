from pages.base_page import *
from time import sleep


def test_logo_is_present(driver):
    """To verify that logo is visible"""
    driver.get(BasePage().url)
    sleep(3)
    find_by_id(driver, BasePage().logo).is_displayed()


def test_start_button_is_visible(driver):
    """To verify that "Start Now" button is visible"""
    driver.get(BasePage().url)
    sleep(3)
    find_by_class(driver, BasePage().start_button).is_displayed()


def test_explore_button_is_visible(driver):
    """To verify that "Explore Back Office button" is visible"""
    driver.get(BasePage().url)
    sleep(3)
    find_by_class(driver, BasePage().explore_button).is_displayed()

import pytest
from pages.base_page import BasePage


@pytest.mark.usefixtures("driver_for_base_test")
class TestBase:

    # def __init__(self, driver):
    #     super().__init__(driver=driver)
    # @pytest.fixture(scope="class")
    # def setup_method(self, driver):
    #     self.driver = driver
    # a = BasePage(driver=None)
    def test_a(self):
        a=1



class TestA(TestBase):
    def test_print_a(self):
        assert 1


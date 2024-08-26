from datetime import time

import pytest
from selenium import webdriver

from base.base_page import BasePage
from page.home_page import HomePage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_order_product(driver):
    print("Test_order_product was srarted")
    base_page = BasePage(driver)
    base_page.open_page()
    home_page = HomePage(driver)
    home_page.open_search_page()
    print("Search page is opened")
    time(3)

from datetime import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.base_page import BasePage
from page.home_page import HomePage
from page.search_result_page import SearchResultPage


@pytest.fixture(scope="function")
def driver():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Запуск в headless режиме
    # Передаем chrome_options в веб-драйвер
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_order_product(driver):
    print("Test_order_product was started")
    base_page = BasePage(driver)
    base_page.open_page()
    base_page.accept_cookies()
    home_page = HomePage(driver)
    home_page.open_search_page()
    print("Search page is opened")
    time(3)
    search_page = SearchResultPage(driver)
    search_page.set_filter_products()
    print("Needed products are chose")
    time(3)

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base_page.base_page import BasePage
from page.home_page import HomePage
from page.making_order_page import MakingOrderPage
from page.product_cart_page import ProductCartPage
from page.search_result_page import SearchResultPage

@pytest.mark.smoke
def test_quest_can_to_order_product(driver):
    print("**test_quest_can_to_order_product** was started")

    url = "https://sila.by/"

    # Инициализация домашней страницы и переход по URL
    home_page = HomePage(driver, url)

    # Обработка accepting cookies
    home_page.accept_cookies_for_starting_page()

    # Открытие страницы поиска
    home_page.click_button_open_notebooks()
    print("Search page is opened")

    # Инициализация страницы результатов поиска
    search_page = SearchResultPage(driver)
    # Выбор фильтров товара
    search_page.set_filter_products()
    print("Needed products are chosen")

    # Открытие карточки
    search_page.open_product_cart()

    # Инициализация страницы карточки товара
    product_cart_page = ProductCartPage(driver)
    time.sleep(5)
    # Добавление товара в корзину и переход к оформлению
    product_cart_page.add_product_to_card_and_go_to_checkout()

    # Инициализация страницы корзины с заказом
    making_order_page = MakingOrderPage(driver)

    user_data = {
        "first_name": "Евгений",
        "last_name": "Павлович",
        "phone": "1234567890",
        "email": "e.pavlovich29@gmail.com",
        "city": "Минск",
        "comments": "Привезите до 19:00",
        "promocode": "15648"
    }

    making_order_page.fill_form_making_order(user_data)


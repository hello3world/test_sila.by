from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class ProductCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    BUTTON_ADD_TO_CART = "//div[@title='В КОРЗИНУ!']"
    POPUP_ORDER = "//div[@class='btn_zak_popup']"

    # Getters
    def get_button_add_to_cart(self):
        return self.wait_and_find_element(self.BUTTON_ADD_TO_CART)

    def get_button_to_place_an_order(self):
        return self.wait_and_find_element(self.POPUP_ORDER)

    # Actions
    def click_button_add_to_cart(self):
        button_add_to_cart = self.get_button_add_to_cart()
        button_add_to_cart.click()

    def click_button_to_place_an_order(self):
        button_to_place_an_order = self.get_button_to_place_an_order()
        button_to_place_an_order.click()

    # Methods
    def add_product_to_card_and_go_to_checkout(self):
        self.click_button_add_to_cart()
        self.click_button_to_place_an_order()
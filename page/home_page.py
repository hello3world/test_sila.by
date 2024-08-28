from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_and_find_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
        except TimeoutException:
            print(f"Element with locator {locator} was not visible within 10 "
                  f"seconds.")

    # Locators
    search_input = "(//input[@name='find'])[2]"
    button_lupa = "(//input[@type='submit'])[2]"
    product = "ноутбук"

    # Getters
    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search_input)))

    def get_button_lupa(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_lupa)))

    # Actions
    def click_to_search_input(self):
        self.get_search_input().click()
        print('complete click_to_search_input')

    def input_search_input(self):
        self.get_search_input().send_keys(self.product)
        print('input_search_input is chosen')

    def click_to_button_lupa(self):
        self.get_button_lupa().click()
        print('complete click_to_button_lupa')

    # Methods
    def open_search_page(self):
        self.click_to_search_input()
        self.input_search_input()
        self.click_to_button_lupa()

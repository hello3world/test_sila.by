from selenium.webdriver.common.by import By

from base.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    search_input = (By.XPATH, "(//input[@name='find'])[2]")
    button_lupa = (By.XPATH, "(//input[@type='submit'])[2]")
    product = "ноутбук"

    # Getters
    def get_search_input(self):
        return self.driver.find_element(*self.search_input)

    def get_button_lupa(self):
        return self.driver.find_element(*self.button_lupa)

    # Actions
    def click_to_search_input(self):
        self.get_search_input().click()
        print('complete click_to_search_input')

    def input_search_input(self):
        self.get_search_input().send_keys(self.product)

    def click_to_button_lupa(self):
        self.get_button_lupa().click()
        print('complete click_to_button_lupa')

    # Methods
    def open_search_page(self):
        self.click_to_search_input()
        self.input_search_input()
        self.click_to_button_lupa()

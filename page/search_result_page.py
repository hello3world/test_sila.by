import time

from selenium.common.exceptions import TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page.base_page import BasePage


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_element_up(self, element, pixels=100):
        # Получаем текущее положение элемента
        current_position = self.driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {top: rect.top + window.pageYOffset};
        """, element)

        # Прокручиваем страницу на указанное количество пикселей вверх
        self.driver.execute_script("""
            window.scrollTo(0, arguments[0] - arguments[1]);
        """, current_position['top'], pixels)

    # Locators
    producer = (By.XPATH, "//a[text()='ASUS']")
    type_prod = (By.XPATH, "//u[text()='Тип']")
    type_playing = (By.XPATH, "//strong[text()='игровой']")
    result_button = (By.XPATH, "//input[@value='Показать']")
    notebook = (By.XPATH, "(//div[@class='prew_params'])[1]")

    # Getters
    def get_producer(self):
        return self.wait_and_find_element(self.producer)

    def get_type(self):
        return self.wait_and_find_element(self.type_prod)

    def get_type_playing(self):
        return self.wait_and_find_element(self.type_playing)

    def get_result_button(self):
        return self.wait_and_find_element(self.result_button)

    def get_notebook(self):
        return self.wait_and_find_element(self.notebook)

    # Actions
    def choose_producer(self):
        element = self.get_producer()
        if element:
            print(f"Element found: {element}")
            self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                       element)
            self.driver.execute_script("arguments[0].click();", element)
            print("choose_producer complete")

    def press_type(self):
        element = self.get_type()
        if element:
            print(f"Element found: {element}")
            self.scroll_element_up(element, 100)
            element.click()
            print("press_type complete")

    def choose_type_playing(self):
        element = self.get_type_playing()
        if element:
            print(f"Element found: {element}")
            self.scroll_element_up(element, 100)
            self.driver.execute_script("arguments[0].click();", element)
            print("choose_type_playing")

    def press_result_button(self):
        element = self.get_result_button()
        if element:
            print(f"Element found: {element}")
            self.scroll_element_up(element, 100)
            self.driver.execute_script("arguments[0].click();", element)
            print("press_result_button")

    def press_notebook(self):
        element = self.get_notebook()
        if element:
            print(f"Element found: {element}")
            self.driver.execute_script("arguments[0].click();", element)
            print("press_notebook complete")

    # Methods
    def set_filter_products(self):
        self.choose_producer()
        self.press_type()
        self.choose_type_playing()
        self.press_result_button()

    def open_product_cart(self):
        self.press_notebook()


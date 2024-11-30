from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from base_page.base_page import BasePage


class MakingOrderPage(BasePage):
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
    INPUT_FIRST_NAME = (By.ID, "first_name")
    INPUT_LAST_NAME = (By.ID, "last_name")
    INPUT_PHONE = (By.ID, "phone_long")
    INPUT_EMAIL = (By.ID, "mail")
    CHECKBOX_PICKUP = (By.CSS_SELECTOR, ".samovyvoz")
    SELECT_CITY = (By.ID, "samovyvoz_city_e1504fa-bq1087_90nb0zr2-m02370")
    CHECKBOX_PAYMENT = (By.ID, "pay_2")
    TEXTAREA_COMMENTS = (By.NAME, "text")
    INPUT_PROMOCODE = (By.ID, "promocode")
    CHECKBOX_AGREEMENT = (By.ID, "switch_btn_cookies")

    # Getters
    def get_input_first_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_FIRST_NAME))

    def get_input_last_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_LAST_NAME))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_PHONE))

    def get_input_email(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_EMAIL))

    def get_checkbox_pickup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKBOX_PICKUP))

    def get_select_city(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SELECT_CITY))

    def get_checkbox_payment(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKBOX_PAYMENT))

    def get_textarea_comments(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TEXTAREA_COMMENTS))

    def get_input_promocode(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_PROMOCODE))

    def get_checkbox_agreement(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKBOX_AGREEMENT))

    # Actions
    def fill_input_first_name(self, first_name):
        input_first_name = self.get_input_first_name()
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def fill_input_last_name(self, last_name):
        input_last_name = self.get_input_last_name()
        input_last_name.clear()
        input_last_name.send_keys(last_name)

    def fill_input_phone(self, phone):
        input_phone = self.get_input_phone()
        input_phone.clear()
        input_phone.send_keys(phone)

    def fill_input_email(self, email):
        input_email = self.get_input_email()
        input_email.clear()
        input_email.send_keys(email)

    def select_pickup(self):
        checkbox_pickup = self.get_checkbox_pickup()
        self.scroll_element_up(checkbox_pickup, 100)
        checkbox_pickup.click()

    def select_city(self, city_name="Минск"):
        dropdown = self.get_select_city()
        select = Select(dropdown)
        select.select_by_index(2)

    def select_payment_option(self):
        self.get_checkbox_payment().click()

    def fill_comments(self, comment):
        textarea_comments = self.get_textarea_comments()
        textarea_comments.clear()
        textarea_comments.send_keys(comment)

    def apply_promocode(self, promocode):
        input_promocode = self.get_input_promocode()
        input_promocode.clear()
        input_promocode.send_keys(promocode)

    def accept_agreement(self):
        self.get_checkbox_agreement().click()

    # Method for filling the entire form
    def fill_form_making_order(self, user_data):
        self.fill_input_first_name(user_data["first_name"])
        self.fill_input_last_name(user_data["last_name"])
        self.fill_input_phone(user_data["phone"])
        self.fill_input_email(user_data["email"])
        self.select_pickup()
      #  self.select_city()  # Default city is Минск
        self.select_payment_option()
        self.fill_comments(user_data["comments"])
        self.apply_promocode(user_data["promocode"])
        self.accept_agreement()

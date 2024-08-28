from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    url = "https://sila.by/"
    button_cookies = "//button[@class='cookies_save']"

    # Actions



    # Methods
    def open_page(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()

    def accept_cookies(self):
        try:
            self.driver.find_element(By.XPATH, self.button_cookies).click()
            print("Cookies accepted")
        except Exception as e:
            print("Cookies acceptance failed: ", e)

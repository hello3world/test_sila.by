from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Locators
    url = "https://sila.by/"
    button_cookies = (By.XPATH, "//button[@class='cookies_save']")

    #Actions
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))


    #Methods
    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def accept_cookies(self):
        try:
            self.driver.find_element(*self.button_cookies).click()
            print("Cookies accepted")
        except Exception as e:
            print("Cookies acceptance failed: ", e)

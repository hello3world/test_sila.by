from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    url = "https://sila.by/"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))

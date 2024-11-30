from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    # Локаторы
    button_open_notebooks_locator = (
By.CSS_SELECTOR, ".block_catalog__item.notebook_sl")

    # Methods
    def click_button_open_notebooks(self):
        self.click_element_with_exceptions(self.button_open_notebooks_locator)

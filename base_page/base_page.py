from selenium.common import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        if self.url:
            self.open_page()  # Автоматически открываем страницу, если URL указан

    # Locators
    button_cookies = (By.XPATH, "//button[@class='cookies_save']")  # Определяем как кортеж

    # Methods
    def open_page(self):
        """Открываем страницу по указанному URL"""
        self.driver.get(self.url)

    def accept_cookies_for_starting_page(self, timeout=10):
        """Ожидаем и нажимаем кнопку cookies, если она существует"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.button_cookies)
            ).click()
            print("Cookies accepted")
        except TimeoutException:
            print("Cookies acceptance timed out.")
        except Exception as e:
            print("Cookies acceptance failed: ", e)

    def click_element_with_exceptions(self, locator):
        max_retries = 3  # количество попыток для обработки StaleElementReferenceException
        attempt = 0
        while attempt < max_retries:
            try:
                # Ожидание кликабельности элемента
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                      element)

                try:
                    # Попытка выполнить клик
                    element.click()
                    print("Clicked on notebooks button")
                    break
                except ElementClickInterceptedException:
                    print(
                        "Element click intercepted. Trying JavaScript click...")
                    # Выполняем JavaScript-клик, если обычный клик перехвачен
                    self.driver.execute_script("arguments[0].click();",
                                          element)
                    print("Clicked on notebooks button using JavaScript")
                    break

            except StaleElementReferenceException:
                attempt += 1
                print(
                    f"StaleElementReferenceException encountered. Retrying... (attempt {attempt}/{max_retries})")
            except TimeoutException:
                print(
                    "Button open notebooks was not clickable within the timeout period.")
                break
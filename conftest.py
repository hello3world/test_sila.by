import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from faker import Faker
#
# fake = Faker()

# Фикстура для инициализации и завершения драйвера
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск в фоновом режиме
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# @pytest.fixture
# def user_data():
#     username = fake.user_name()
#     password = fake.password()
#     return {"username": username, "password": password}
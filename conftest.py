import pytest
from selenium import webdriver


@pytest.fixture()
def setUp_tearDown():
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_argument("--disable-save-password-bubble")
    option.add_argument("--password-store=basic")
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()

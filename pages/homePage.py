import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import TestConstant
from selenium import webdriver

class HomePage:
    lbl_4th_sku_name = (By.XPATH, '//div[contains(text(),"Sauce Labs Onesie")]')
    btn_addToCart = ('//div[normalize-space()="{}"]'
                     '/ancestor::div[@class="inventory_item"]//button')

    @allure.step('Verify user successfully navigated to home page.')
    def verify_success_login(self,driver: webdriver):
        try:
            lbl_assetHomePage = WebDriverWait(driver, TestConstant.wait_time.value).until(
                    EC.presence_of_element_located(self.lbl_4th_sku_name))
            return lbl_assetHomePage.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Add item to cart')
    def add_item_to_cart(self,driver: webdriver,sku_name: str):
        driver.find_element(*self.format_add_to_cart_locator(sku_name)).click()

    @staticmethod
    def format_add_to_cart_locator(sku_name):
        return (By.XPATH, HomePage.btn_addToCart.format(sku_name))
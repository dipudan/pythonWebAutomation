import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderCompletion:
    lbl_confirmation = (By.XPATH,"//*[contains(text(),'Thank you for your order!')]")

    @allure.step('Verify order is placed successfully')
    def verifyOrder(self,driver: webdriver)-> None:
        assert driver.find_element(*self.lbl_confirmation).is_displayed()== True
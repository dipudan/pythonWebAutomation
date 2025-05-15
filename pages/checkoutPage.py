import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckoutPage:
    lnk_cart_icon = (By.CLASS_NAME, 'shopping_cart_link')
    btn_chkOut = (By.NAME, 'checkout')
    txt_firstName = (By.NAME, 'firstName')
    txt_lastName = (By.NAME, 'lastName')
    txt_zipcode = (By.NAME, 'postalCode')
    btn_continue = (By.ID, 'continue')
    btn_finish =(By.ID, 'finish')

    @allure.step('Checking out item added to cart.')
    def checkout_item(self, driver: webdriver, fname: str, lname: str, zip: str):
        driver.find_element(*self.lnk_cart_icon).click()
        driver.find_element(*self.btn_chkOut).click()
        driver.find_element(*self.txt_firstName).send_keys(fname)
        driver.find_element(*self.txt_lastName).send_keys(lname)
        driver.find_element(*self.txt_zipcode).send_keys(zip)
        driver.find_element(*self.btn_continue).click()
        driver.find_element(*self.btn_finish).click()

import time

import allure
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants import TestConstant

class LoginPage:
    txt_username = (By.ID, 'user-name')
    txt_password = (By.ID, 'password')
    btn_login = (By.ID, 'login-button')

    @allure.step('Login to the application.')
    def login_to_application(self,driver: webdriver ,username: str,password: str)-> None:
        driver.get(TestConstant.baseUrl.value)
        driver.find_element(*self.txt_username).send_keys(username)
        driver.find_element(*self.txt_password).send_keys(password)
        driver.find_element(*self.btn_login).click()
        time.sleep(5)
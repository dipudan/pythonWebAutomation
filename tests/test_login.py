import allure
from allure_commons.types import Severity
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage

@pytest.mark.parametrize('username,password',[("standard_user","secret_sauce")])
@allure.title("Login with valid user. Users :- {username} , {password}")
@allure.severity(Severity.CRITICAL)
def test_login(setUp_tearDown,username: str,password: str):
    driver = setUp_tearDown
    login_page = LoginPage()
    home_page = HomePage()

    login_page.login_to_application(driver,username,password)
    assert home_page.verify_success_login(driver) == True, 'Verify login to home page is successful'
    setUp_tearDown

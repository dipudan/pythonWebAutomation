import allure
import pytest
from allure_commons.types import Severity

from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.checkoutPage import CheckoutPage
from pages.orderConfirmation import OrderCompletion


@pytest.mark.parametrize('username, password,sku, fname, lname, zip',
                         [("standard_user", "secret_sauce",
                           "Sauce Labs Backpack", "Dipu", "Krishnan", "10243")])
@allure.title("Add item to cart and checkout.")
@allure.severity(Severity.CRITICAL)
def test_checkout(setUp_tearDown, username : str, password : str,
                  sku : str, fname : str, lname : str, zip : str):
    driver = setUp_tearDown
    login_page = LoginPage()
    home_page = HomePage()
    checkout_page = CheckoutPage()
    orderConf_page = OrderCompletion()

    login_page.login_to_application(driver, username, password)
    home_page.add_item_to_cart(driver, sku)
    checkout_page.checkout_item(driver, fname, lname, zip)
    orderConf_page.verifyOrder(driver)
    setUp_tearDown

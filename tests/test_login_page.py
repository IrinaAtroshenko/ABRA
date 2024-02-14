# import allure
# from allure_commons.types import AttachmentType
from pages.login_page import LoginPage
from locators.variables import LoginPageConstants
# import os
# from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.login_page_locators import LoginPageLocators


# @allure.feature('user_login')
# @allure.story('Login with correct data')
# @allure.severity('blocker')
def test_login_with_correct_data(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_password()
    page.submit_login()
    # with allure.step('main page is opened after successful login.'):
    #     allure.attach(browser.get_screenshot_as_png(), name='login_result', attachment_type=AttachmentType.PNG)
    account_icon = page.check_account_icon()
    assert account_icon, 'account_icon is not found within 10 seconds'


# @allure.feature('user_login')
# @allure.story('Login with incorrect data: email + password')
# @allure.severity('blocker')
def test_login_with_incorrect_data(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_unregistered_email()
    page.enter_incorrect_password()
    page.submit_login()
    error_message = wait.until(ec.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageConstants.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Expected error message is not displayed"
    assert expected_url == current_url, "URLs do not match"


# @allure.feature('user_login')
# @allure.story('Login with incorrect password')
# @allure.severity('blocker')
def test_login_with_incorrect_password(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_email()
    page.enter_incorrect_password()
    page.submit_login()
    error_message = wait.until(ec.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageConstants.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Expected error message is not displayed"
    assert expected_url == current_url, "URLs do not match"


# @allure.feature('user_login')
# @allure.story('Login with unregistered email')
# @allure.severity('blocker')
def test_login_with_unregistered_email(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_unregistered_email()
    page.enter_password()
    page.submit_login()
    error_message = wait.until(ec.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageConstants.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Expected error message is not displayed"
    assert expected_url == current_url, "URLs do not match"


# @allure.feature('user_login')
# @allure.story('Login button with correct email + empty password')
# @allure.severity('critical')
def test_login_with_empty_password(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    login_btn = page.check_login_btn()
    assert not login_btn.is_enabled(), "Login button is available"


# @allure.feature('user_login')
# @allure.story('Login button with empty email + password')
# @allure.severity('critical')
def test_login_with_empty_email(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_password()
    login_btn = page.check_login_btn()
    assert not login_btn.is_enabled(), "Login button is available"


# @allure.feature('user_login')
# @allure.story('Login with invalid email')
# @allure.severity('critical')
def test_login_with_invalid_email(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_invalid_email()
    page.enter_password()
    login_btn = page.check_login_btn()
    assert not login_btn.is_enabled(), "Login button is available"


# @allure.feature('user_login')
# @allure.story('Login with password less than 8 characters long')
# @allure.severity('critical')
def test_login_with_short_pass(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_short_password()
    login_btn = page.check_login_btn()
    assert not login_btn.is_enabled(), "Login button is available"

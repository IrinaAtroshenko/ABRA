import chromedriver_autoinstaller
from selenium import webdriver
import pytest
# import allure
# from allure_commons.types import AttachmentType
from pages.login_page import LoginPage
from locators.variables import LoginPageConstants
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.login_page_locators import LoginPageLocators


@pytest.fixture()
def browser():
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(autouse=False)
def login(browser):
    link = LoginPageConstants.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_email()
    page.enter_password()
    page.submit_login()
    # with allure.step('home page is opened after successful login.'):
    #     allure.attach(browser.get_screenshot_as_png(), name='home_page', attachment_type=AttachmentType.PNG)
    account_icon = wait.until(ec.visibility_of_element_located(LoginPageLocators.ACCOUNT_ICON))
    assert account_icon, 'account_icon is not found within 10 seconds'

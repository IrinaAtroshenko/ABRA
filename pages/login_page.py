from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.variables import LoginPageConstants


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageConstants.LOGIN_CORRECT_EMAIL)

    def enter_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(LoginPageConstants.LOGIN_CORRECT_PASS)

    def submit_login(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def check_account_icon(self):
        account_icon = self.browser.find_element(*LoginPageLocators.ACCOUNT_ICON)
        return account_icon

    def enter_unregistered_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageConstants.LOGIN_INCORRECT_EMAIL)

    def enter_incorrect_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(LoginPageConstants.LOGIN_INCORRECT_PASS)

    def enter_invalid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageConstants.LOGIN_INVALID_EMAIL)

    def check_login_btn(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        return login_button

    def enter_short_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(LoginPageConstants.LOGIN_SHORT_PASS)

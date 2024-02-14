from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[1]/input')
    LOGIN_PASS = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')
    ACCOUNT_ICON = (By.XPATH, '//*[@id="header-popup"]/li[4]/button/div')
    ERROR_MESSAGE = (By.XPATH, '/html/body/div[2]/p')
    ERROR_MSG_EMPTY_PASS = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/span')

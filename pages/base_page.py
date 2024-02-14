from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return Wait(self.browser, timeout).until(ec.element_to_be_clickable(locator))



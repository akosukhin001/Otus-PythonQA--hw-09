from .BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    TITLE = 'Administration'
    PANEL_TEXT = (css, ".panel-title")
    USERNAME = (css, '#input-username')
    PASSWORD = (css, '#input-password')
    LOGIN_BTN = (css, '.fa.fa-key')
    FORGOTTEN_PASSWORD = (css, '.help-block')

    def check_title(self):
        self.logger.info('check_title')
        return self.TITLE

    def check_panel_text(self):
        self.logger.info('check_panel_text')
        return self._get_element_text(self.PANEL_TEXT, 0)

    def input_username(self, value):
        self.logger.info('input_username')
        return self._input(self.USERNAME, value)

    def input_password(self, value):
        self.logger.info('input_password')
        return self._input(self.PASSWORD, value)

    def click_login_button(self):
        self.logger.info('click_login_button')
        return self._click(self.LOGIN_BTN)

    def click_forgotten_password(self):
        self.logger.info('click_forgotten_password')
        return self._click(self.FORGOTTEN_PASSWORD)


from .BasePage import BasePage
from selenium.webdriver.common.by import By
import pytest, allure


class AdminLoginPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    TITLE = 'Administration'
    PANEL_TEXT = (css, ".panel-title")
    USERNAME = (css, '#input-username')
    PASSWORD = (css, '#input-password')
    LOGIN_BTN = (css, '.fa.fa-key')
    FORGOTTEN_PASSWORD = (css, '.help-block')

    @allure.description('AdminLoginPage')
    @allure.story('AdminLoginPage')
    def check_title(self):
        with allure.step("Проверяем title"):
            return self.TITLE

    @pytest.mark.AdminLoginPage
    def check_panel_text(self):
        with allure.step(""):
            return self._get_element_text(self.PANEL_TEXT, 0)

    @pytest.mark.AdminLoginPage
    def input_username(self, value):
        with allure.step(""):
            return self._input(self.USERNAME, value)

    @pytest.mark.AdminLoginPage
    def input_password(self, value):
        with allure.step(""):
            return self._input(self.PASSWORD, value)

    @pytest.mark.AdminLoginPage
    def click_login_button(self):
        with allure.step(""):
            return self._click(self.LOGIN_BTN)

    @pytest.mark.AdminLoginPage
    def click_forgotten_password(self):
        with allure.step(""):
            return self._click(self.FORGOTTEN_PASSWORD)


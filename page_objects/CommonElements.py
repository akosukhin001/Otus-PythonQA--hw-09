from selenium.webdriver.common.by import By
from page_objects import BasePage
import allure


class CommonElements(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    CART = (css, '#cart-total')
    NAV_LINKS = (css, 'ul.nav > li')
    SEARCH = (css, '[name=search]')
    CURRENCY = (css, '#form-currency')

    def click_cart(self):
        self.logger.info('click_cart')
        with allure.step("кликаем cart"):
            self._click((self.CART))
            return self

    def find_nav_links(self):
        self.logger.info('find_nav_links')
        with allure.step("ищем nav_links"):
            self._element(self.NAV_LINKS)
            return self

    def search(self):
        self.logger.info('search')
        with allure.step("вводим тестовую строку в поиск"):
            self._input(self.SEARCH, 'test_input_string')
            return self

    def find_currency(self):
        self.logger.info('find_currency')
        with allure.step("ищем валюту хахаха"):
            self._element(self.CURRENCY)
            return self


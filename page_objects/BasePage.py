from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging


class BasePage():

    def __init__(self, wd):
        self.wd = wd
        self.logger = logging.getLogger(type(self).__name__)

    def _element(self, selector: tuple, index: int = 0):
        with allure.step(f"ищем элемент по селектору {selector}"):
            return self.wd.find_elements(*selector)[index]

    def _elements(self, selector: tuple):
        with allure.step(f"ищем элементы по селектору {selector}"):
            return self.wd.find_elements(*selector)

    def _click(self, selector: tuple):
        with allure.step(f"кликаем по элементу - селектор {selector}"):
            ActionChains(self.wd).move_to_element(self._element(selector)).click().perform()

    def _input(self, selector: tuple, value):
        with allure.step(f"вводим {value} в элемент с селектором {selector}"):
            element = self._element(selector)
            element.clear()
            element.send_keys(value)

    def _get_element_text(self, selector: tuple, index):
        with allure.step(f"читаем текст из элемента с селектором {selector}"):
            return self._element(selector, index).text

    def _wait_for_text_to_be_present_in_element(self, selector, wait, text=None):
        with allure.step(f"ожидаем появления элемента с селектором {selector}"):
            return wait.until(EC.text_to_be_present_in_element((selector), text))

    def _wait_for_presence_of_element_located(self, selector, wait):
        with allure.step(f"ожидаем присутствия элемента с селектором {selector}"):
            return wait.until(EC.presence_of_element_located((selector)))

    def _wait_for_visible(self, selector: tuple, index, wait=3):
        with allure.step(f"ожидаем видимости элемента с селектором {selector}"):
            return WebDriverWait(self.wd, wait).until(EC.visibility_of(self._element((selector), index)))

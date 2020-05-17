from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, wd):
        self.wd = wd

    def _element(self, selector: tuple, index: int = 0):
        return self.wd.find_elements(*selector)[index]

    def _elements(self, selector: tuple):
        return self.wd.find_elements(*selector)

    def _click(self, selector: tuple):
        ActionChains(self.wd).move_to_element(self._element(selector)).click().perform()

    def _input(self, selector: tuple, value):
        element = self._element(selector)
        element.clear()
        element.send_keys(value)

    def _get_element_text(self, selector: tuple, index):
        return self._element(selector, index).text

    def _wait_for_text_to_be_present_in_element(self, selector, wait, text=None):
        return wait.until(EC.text_to_be_present_in_element((selector), text))

    def _wait_for_presence_of_element_located(self, selector, wait):
        return wait.until(EC.presence_of_element_located((selector)))

    def _wait_for_visible(self, selector: tuple, index, wait=3):
        return WebDriverWait(self.wd, wait).until(EC.visibility_of(self._element((selector), index)))

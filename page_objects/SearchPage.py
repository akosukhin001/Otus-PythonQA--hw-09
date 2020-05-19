from .BasePage import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    KEYWORDS = (css, '#input-search')
    ALL_CATEGORIES = (css, 'select[name="category_id"]')
    IN_DESCR_CHECKBOX = (css, '#description')
    IN_SUBCAT_CHECKBOX = (css, '[name=sub_category]')
    SEARCH_BTN = (css, '#button-search')

    def keyword_input(self, value):
        return self._input(self.KEYWORDS, value)

    def click_categories_select(self):
        return self._click(self.ALL_CATEGORIES)

    def check_descr_checkbox(self):
        return self._element(self.IN_DESCR_CHECKBOX)

    def check_subcat_checkbox(self):
        return self._element(self.IN_SUBCAT_CHECKBOX)

    def click_search_button(self):
        return self._click(self.SEARCH_BTN)
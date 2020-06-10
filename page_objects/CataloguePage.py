from .BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class CataloguePage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    FEATURED = (css, 'div.row .product-layout')
    ITEMS_LIST = (css, '#column-left > .list-group')
    LIST_VIEW_BTN = (css, '#list-view')
    GRID_VIEW_BTN = (css, '#grid-view')
    SORT_SELECT = (css, '#input-sort')
    SHOW_QTY_SELECT = (css, '#input-limit')

    def click_featured(self):
        self.logger.info('click_featured')
        with allure.step("кликаем на featured"):
            return self._click(self.FEATURED)

    def check_items_list(self):
        self.logger.info('check_items_list')
        with allure.step("получение списка эл-тов"):
            return self._elements(self.ITEMS_LIST)

    def click_list_view_button(self):
        self.logger.info('click_list_view_button')
        with allure.step("кликаем на list_view_button"):
            return self._click(self.LIST_VIEW_BTN)

    def click_grid_view_btn(self):
        self.logger.info('click_grid_view_btn')
        with allure.step("кликаем на grid_view_btn"):
            return self._click(self.GRID_VIEW_BTN)

    def check_sort_select(self):
        self.logger.info('check_sort_select')
        with allure.step("проверяем"):
            return self._element(self.SORT_SELECT)

    def check_show_qty_select(self):
        self.logger.info('check_show_qty_select')
        with allure.step("проверяем количество"):
            return self._element(self.SHOW_QTY_SELECT)

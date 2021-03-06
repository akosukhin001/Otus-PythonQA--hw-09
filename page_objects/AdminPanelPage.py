from .BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminPanelPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    ADD_NEW_BTN = (css, '.fa-plus')
    COPY_BTN = (css, '.fa-copy')
    DELETE_BTN = (css, '.btn-danger')
    PRODUCT_NAME_INPUT = (css, '#input-name1')
    META_TAG_INPUT = (css, '#input-meta-title1')
    DATA_TAB = (link_text, 'Data')
    MODEL_INPUT = (css, '#input-model')
    SAVE_BTN = (css, '.fa-save')
    SUCCESS_ALERT = (css, '.alert-success')
    EDIT_BTN = (css, '[data-original-title="Edit"]')
    INPUT_PRICE = (css, '#input-price')
    CHECKBOX = (css, '[name="selected[]"]')
    TABLE = (css, 'tbody')
    NEXT_PAGE = (link_text, '>')
    PAGE_PAGINATION = (css, '.pagination')

    def click_add_new_button(self):
        self.logger.info('click_add_new_button')
        with allure.step("кликаем на add_new_button"):
            return self._click(self.ADD_NEW_BTN)

    def wait_for_product_name_input(self):
        self.logger.info('wait_for_product_name_input')
        with allure.step("ожидаем появления"):
            # return self._wait_for_visible(self.PRODUCT_NAME_INPUT, index=0)
            return self._wait_for_visible(self.PRODUCT_NAME_INPUT, index=0)

    def input_product_name(self, value):
        self.logger.info('input_product_name')
        with allure.step("вводим имя продукта"):
            return self._input(self.PRODUCT_NAME_INPUT, value)

    def input_meta_tag(self, value):
        self.logger.info('input_meta_tag')
        with allure.step("вводим мета тег"):
            return self._input(self.META_TAG_INPUT, value)

    def click_data_tab(self):
        self.logger.info('click_data_tab')
        with allure.step("переходим на вкладку data"):
            return self._click(self.DATA_TAB)

    def input_model(self, value):
        self.logger.info('input_model')
        with allure.step("вводим модель"):
            return self._input(self.MODEL_INPUT, value)

    def click_save_button(self):
        self.logger.info('click_save_button')
        with allure.step("сохраняем"):
            return self._click(self.SAVE_BTN)

    def wait_for_success_alert(self):
        self.logger.info('wait_for_success_alert')
        with allure.step("ожидаем появления подтверждения успеха"):
            return self._wait_for_visible(self.SUCCESS_ALERT, index=0)

    def click_edit_button(self):
        self.logger.info('click_edit_button')
        with allure.step("редактируем"):
            return self._click(self.EDIT_BTN)

    def input_price(self, value):
        self.logger.info('input_price')
        with allure.step("вводим цену"):
            return self._input(self.INPUT_PRICE, value)

    def products_amount(self):
        self.logger.info('products_amount')
        with allure.step("количество продуктов"):
            table_body = self._element(self.TABLE)
            self.products_qty = int(table_body.get_attribute('childElementCount'))
            return self.products_qty

    def click_next_page(self):
        self.logger.info('click_next_page')
        with allure.step("переходим на след страницу"):
            return self._click(self.NEXT_PAGE)

    def click_last_element(self):
        self.logger.info('click_last_element')
        with allure.step("последний элемент"):
            return self._element(self.CHECKBOX, index=-1).click()

    def click_delete_button(self):
        self.logger.info('click_delete_button')
        with allure.step("удаляем"):
           return self._click(self.DELETE_BTN)

    def check_page_pagination(self):
        self.logger.info('check_page_pagination')
        with allure.step("проверяем пагинацию"):
            try:
                self._element(self.PAGE_PAGINATION)
                return True
            except IndexError:
                print('\nEXACTLY 20 ITEMS -> no pagination!')
                return False

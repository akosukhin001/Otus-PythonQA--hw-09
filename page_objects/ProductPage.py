from .BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class ProductPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    CART = (css, '#cart-total')
    CART_STATUS = (css, '.text-center')
    ALERT_MESSAGE = (css, '.alert')
    WISH_LIST_BTN = (css, '[data-original-title="Add to Wish List"]')
    COMPARE_BTN = (css, '[data-original-title="Compare this Product"]')
    PRODUCT_DETAILS = (css, 'ul.nav.nav-tabs > li')
    DELIVERY_DATE = (css, 'button.btn.btn-default > i.fa.fa-calendar')
    PRODUCT_QTY = (css, '#input-quantity')
    ADD_TO_CART_BTN = (css, '#button-cart')

    def click_cart(self):
        with allure.step("кликаем корзину"):
            return self._click(self.CART)

    def check_cart_status(self, wait, text):
        with allure.step("проверяем статус корзины"):
            return self._wait_for_text_to_be_present_in_element((self.CART_STATUS), wait, text)

    def click_fishlist_button(self):
        with allure.step("добавляем в вишлист (ну или в рыбалист)"):
            return self._click(self.WISH_LIST_BTN)

    def check_wishlist_alert(self, wait):
        with allure.step("ожидаем подтверждения"):
            return self._wait_for_presence_of_element_located((self.ALERT_MESSAGE), wait)

    def click_compare_button(self):
        with allure.step("сравниваем"):
            return self._click(self.COMPARE_BTN)

    def check_compare_alert(self, wait):
        with allure.step("ожидаем сравнения"):
            return self._wait_for_presence_of_element_located((self.ALERT_MESSAGE), wait)

    def click_product_details_tabs(self):
        with allure.step("переходим по табам с деталями"):
            details = self._elements(self.PRODUCT_DETAILS)
            for detail in details:
                detail.click()

    def click_delivery_date(self):
        with allure.step("кликаем на дате доставки"):
            return self._click(self.DELIVERY_DATE)

    def set_product_qty(self, value):
        with allure.step("устанавливаем кол-во продуктов"):
            return self._input(self.PRODUCT_QTY, value)

    def click_add_to_cart_button(self):
        with allure.step("добваляем в корзину"):
            return self._click(self.ADD_TO_CART_BTN)



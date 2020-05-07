from locators import ProductPage
from time import sleep


def test_cart(browser_product):
    cart = browser_product.find_element_by_css_selector(ProductPage.CART)
    cart.click()


def test_wish_list_button(browser_product):
    browser_product.find_element_by_css_selector(ProductPage.WISH_LIST_BTN)


def test_compare_button(browser_product):
    browser_product.find_element_by_css_selector(ProductPage.COMPARE_BTN)


def test_product_details(browser_product):
    details = browser_product.find_elements_by_css_selector(ProductPage.PRODUCT_DETAILS)
    for detail in details:
        detail.click()


def test_delivery_date(browser_product):
    browser_product.find_element_by_css_selector(ProductPage.DELIVERY_DATE).click()


def test_delivery_date(browser_product):
    browser_product.find_element_by_css_selector(ProductPage.DELIVERY_DATE).click()


def test_add_product(browser_product):
    quantity = browser_product.find_element_by_css_selector(ProductPage.PRODUCT_QTY)
    quantity.clear()
    quantity.input_text(2)


def test_add_product(browser_product):
    button_cart = browser_product.find_element_by_css_selector(ProductPage.ADD_TO_CART_BTN)
    for i in range(3):
        button_cart.click()
        sleep(1)

from locators import ProductPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_cart(browser_product):
    wd, wait = browser_product
    print(wd, wait)
    cart = wd.find_element_by_css_selector(ProductPage.CART)
    cart.click()
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ProductPage.CART_STATUS), 'Your shopping cart is empty!'))


def test_wish_list_button(browser_product):
    wd, wait = browser_product
    wd.find_element_by_css_selector(ProductPage.WISH_LIST_BTN).click()
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductPage.ALERT_MESSAGE)))
    except NoSuchElementException:
        print('logged in user')


def test_compare_button(browser_product):
    wd, wait = browser_product
    wd.find_element_by_css_selector(ProductPage.COMPARE_BTN).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ProductPage.ALERT_MESSAGE)))


def test_product_details(browser_product):
    wd, wait = browser_product
    details = wd.find_elements_by_css_selector(ProductPage.PRODUCT_DETAILS)
    for detail in details:
        detail.click()


def test_delivery_date(browser_product):
    wd, wait = browser_product
    wd.find_element_by_css_selector(ProductPage.DELIVERY_DATE).click()


def test_add_product_qty(browser_product):
    wd, wait = browser_product
    quantity = wd.find_element_by_css_selector(ProductPage.PRODUCT_QTY)
    quantity.clear()
    quantity.send_keys(2)
    quantity.send_keys(Keys.ENTER)


def test_add_product_btn(browser_product):
    wd, wait = browser_product
    button_cart = wd.find_element_by_css_selector(ProductPage.ADD_TO_CART_BTN)
    for i in range(3):
        button_cart.click()
        sleep(1)

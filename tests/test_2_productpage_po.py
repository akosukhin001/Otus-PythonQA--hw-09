from page_objects import ProductPage
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def test_cart(browser_product):
    wd, wait = browser_product
    print(wd, wait)
    ProductPage(wd).click_cart()
    ProductPage(wd).check_cart_status(wait, 'Your shopping cart is empty!')
    sleep(5)


def test_wish_list_button(browser_product):
    '''you need to set expl_wait in cmd-option to pass the test'''
    wd, wait = browser_product
    ProductPage(wd).click_fishlist_button()
    try:
        ProductPage(wd).check_wishlist_alert(wait)
        sleep(3)
    except NoSuchElementException:
        print('logged in user')


def test_compare_button(browser_product):
    '''you need to set expl_wait in cmd-option to pass the test'''
    wd, wait = browser_product
    ProductPage(wd).click_compare_button()
    ProductPage(wd).check_compare_alert(wait)


def test_product_details(browser_product):
    wd, wait = browser_product
    ProductPage(wd).click_product_details_tabs()


def test_delivery_date(browser_product):
    wd, wait = browser_product
    ProductPage(wd).click_delivery_date()


def test_add_product_qty(browser_product):
    wd, wait = browser_product
    ProductPage(wd).set_product_qty(2)
    ProductPage(wd).click_add_to_cart_button()


def test_add_product_btn(browser_product):
    wd, wait = browser_product
    for i in range(3):
        ProductPage(wd).click_add_to_cart_button()
        sleep(1)

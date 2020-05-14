from selenium.webdriver.common.by import By
from locators import CommonElements
from time import sleep


def test_cart(browser_params):
    cart = browser_params.find_element(*CommonElements.CART)
    cart.click()


def test_nav_links(browser_params):
    browser_params.find_elements(*CommonElements.NAV_LINKS)


def test_search(browser_params):
    search = browser_params.find_element(*CommonElements.SEARCH)
    search.send_keys('test')
    sleep(3)
    search.clear()
    sleep(3)


def test_currency(browser_params):
    browser_params.find_element(*CommonElements.CURRENCY)

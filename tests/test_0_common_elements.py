from selenium.webdriver.common.by import By
from locators import CommonElements


def test_cart(browser_params):
    cart = browser_params.find_element_by_css_selector(CommonElements.CART)
    cart.click()


def test_nav_links(browser_params):
    browser_params.find_elements_by_css_selector(CommonElements.NAV_LINKS)


def test_search(browser_params):
    search = browser_params.find_element(By.CSS_SELECTOR, CommonElements.SEARCH)
    search.send_keys('test')
    search.clear()


def test_currency(browser_params):
    browser_params.find_element(By.CSS_SELECTOR, CommonElements.CURRENCY)

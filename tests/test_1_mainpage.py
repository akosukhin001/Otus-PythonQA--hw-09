from selenium.webdriver.common.by import By
from locators import MainPage


# to test an element from CommonElement class
def test_cart(browser_params):
    cart = browser_params.find_element_by_css_selector(MainPage.CART)
    cart.click()


def test_featured(browser_params):
    featured = (By.CSS_SELECTOR, MainPage.FEATURED)
    products = browser_params.find_elements(*featured)
    assert len(products) == 4


def test_promoblock(browser_params):
    promoblock = (By.CSS_SELECTOR, MainPage.PROMOBLOCK)
    browser_params.find_element(*promoblock).click()


def test_promopaginator(browser_params):
    browser_params.find_element_by_css_selector(MainPage.PROMOPAGINATOR)


def test_adverb(browser_params):
    browser_params.find_element_by_css_selector(MainPage.ADV)


def test_advpaginator(browser_params):
    browser_params.find_element_by_css_selector(MainPage.ADVPAGINATOR)

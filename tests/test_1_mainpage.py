from locators import MainPage
from time import sleep


# to test an element from CommonElement class
def test_cart(browser_params):
    cart = browser_params.find_element(*MainPage.CART)
    cart.click()
    sleep(3)


def test_featured(browser_params):
    products = browser_params.find_elements(*MainPage.FEATURED)
    assert len(products) == 4


def test_promoblock(browser_params):
    browser_params.find_element(*MainPage.PROMOBLOCK).click()


def test_promopaginator(browser_params):
    browser_params.find_element(*MainPage.PROMOPAGINATOR)


def test_adverb(browser_params):
    browser_params.find_element(*MainPage.ADV)


def test_advpaginator(browser_params):
    browser_params.find_element(*MainPage.ADVPAGINATOR)

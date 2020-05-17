from page_objects import MainPage
from time import sleep


def test_featured(browser_params):
    product_text = MainPage(browser_params).find_featured(0)
    print(product_text)


def test_promoblock(browser_params):
    MainPage(browser_params).click_promoblock()


def test_promopaginator(browser_params):
    MainPage(browser_params).find_promopaginator()


def test_adverb(browser_params):
    MainPage(browser_params).find_adverb()


def test_advpaginator(browser_params):
    MainPage(browser_params).find_advpaginator()
    sleep(3)
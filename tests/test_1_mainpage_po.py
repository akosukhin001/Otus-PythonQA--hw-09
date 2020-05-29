from page_objects import MainPage
from time import sleep
import logging


def test_featured(browser_with_listener):
    product_text = MainPage(browser_with_listener).find_featured(0)
    print(product_text)


def test_promoblock(browser_with_listener):
    MainPage(browser_with_listener).click_promoblock()


def test_promopaginator(browser_with_listener):
    MainPage(browser_with_listener).find_promopaginator()


def test_adverb(browser_with_listener):
    MainPage(browser_with_listener).find_adverb()


def test_advpaginator(browser_with_listener):
    browser_with_listener.execute_script('console.warn("This is WARNING")')
    MainPage(browser_with_listener).find_advpaginator()
    # sleep(3)

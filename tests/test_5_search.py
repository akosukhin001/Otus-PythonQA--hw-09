from locators import SearchPage
from time import sleep


def test_keyword_input(browser_search):
    search_input = browser_search.find_element(*SearchPage.KEYWORDS)
    search_input.send_keys('HTC')


def test_categories_select(browser_search):
    browser_search.find_element(*SearchPage.ALL_CATEGORIES).click()
    sleep(3)


def test_descr_checkbox(browser_search):
    browser_search.find_element(*SearchPage.IN_DESCR_CHECKBOX)


def test_subcat_checkbox(browser_search):
    browser_search.find_element(*SearchPage.IN_SUBCAT_CHECKBOX)


def test_search_button(browser_search):
    sleep(3)
    browser_search.find_element(*SearchPage.SEARCH_BTN).click()
    sleep(3)

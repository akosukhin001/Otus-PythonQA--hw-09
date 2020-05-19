from page_objects.SearchPage import SearchPage
from time import sleep


def test_keyword_input(browser_search):
    SearchPage(browser_search).keyword_input('HTC')


def test_categories_select(browser_search):
    SearchPage(browser_search).click_categories_select()


def test_descr_checkbox(browser_search):
    SearchPage(browser_search).check_descr_checkbox()


def test_subcat_checkbox(browser_search):
    SearchPage(browser_search).check_subcat_checkbox()


def test_search_button(browser_search):
    SearchPage(browser_search).click_search_button()

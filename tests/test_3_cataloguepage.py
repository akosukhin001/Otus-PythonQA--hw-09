from locators import CataloguePage
from time import sleep


def test_featured(browser_catalogue):
    browser_catalogue.find_element_by_css_selector(CataloguePage.FEATURED).click()


def test_items_list(browser_catalogue):
    items_list = browser_catalogue.find_elements_by_css_selector(CataloguePage.ITEMS_LIST)


def test_list_view_btn(browser_catalogue):
    browser_catalogue.find_element_by_css_selector(CataloguePage.LIST_VIEW_BTN).click()
    sleep(2)


def test_grid_view_btn(browser_catalogue):
    browser_catalogue.find_element_by_css_selector(CataloguePage.GRID_VIEW_BTN).click()


def test_sort_select(browser_catalogue):
    browser_catalogue.find_element_by_css_selector(CataloguePage.SORT_SELECT)


def test_show_qty_select(browser_catalogue):
    browser_catalogue.find_element_by_css_selector(CataloguePage.SHOW_QTY_SELECT)
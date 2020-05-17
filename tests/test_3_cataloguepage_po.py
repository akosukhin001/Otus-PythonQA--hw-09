from page_objects import CataloguePage


def test_featured(browser_catalogue):
    CataloguePage(browser_catalogue).click_featured()


def test_items_list(browser_catalogue):
    CataloguePage(browser_catalogue).check_items_list()


def test_list_view_btn(browser_catalogue):
    CataloguePage(browser_catalogue).click_list_view_button()


def test_grid_view_btn(browser_catalogue):
    CataloguePage(browser_catalogue).click_grid_view_btn()


def test_sort_select(browser_catalogue):
    CataloguePage(browser_catalogue).check_sort_select()


def test_show_qty_select(browser_catalogue):
    CataloguePage(browser_catalogue).check_show_qty_select()

from page_objects import CommonElements


def test_cart(browser_params):
    CommonElements(browser_params).click_cart()


def test_nav_links(browser_params):
    CommonElements(browser_params).find_nav_links()


def test_search(browser_params):
    CommonElements(browser_params).search()


def test_currency(browser_params):
    CommonElements(browser_params).find_currency()

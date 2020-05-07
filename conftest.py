from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--url', '-U', default='http://localhost')
    parser.addoption('--browser', '-B', choices=['Chrome', 'Firefox'], default='Chrome')


@pytest.fixture
def browser_params(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)
    # wd.implicitly_wait(20)
    request.addfinalizer(wd.close)
    return wd


@pytest.fixture
def browser_product(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/index.php?route=product/product&path=18&product_id=47'
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)
    request.addfinalizer(wd.close)
    return wd


@pytest.fixture
def browser_catalogue(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/index.php?route=product/category&path=20_27'
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)
    request.addfinalizer(wd.close)
    return wd


@pytest.fixture
def browser_admin_login(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/admin/'
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)
    request.addfinalizer(wd.close)
    return wd


@pytest.fixture
def browser_search(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/index.php?route=product/search'
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)
    request.addfinalizer(wd.close)
    return wd

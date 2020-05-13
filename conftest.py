from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption('--url', '-U', default='http://localhost')
    parser.addoption('--browser', '-B', choices=['Chrome', 'Firefox'], default='Chrome')
    parser.addoption('--expl_wait', '-E', type=int, required=None, default=0, help='explicit wait in seconds')
    parser.addoption('--impl_wait', '-I', type=int, required=None, help='explicit wait in seconds')



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
    expl_wait = request.config.getoption('--expl_wait')
    impl_wait = request.config.getoption('--impl_wait')

    url = 'http://localhost/index.php?route=product/product&path=18&product_id=47'
    if browser == 'Chrome':
        wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wait = WebDriverWait(wd, expl_wait)
    if impl_wait:
        wd.implicitly_wait(impl_wait)
    print('\nexpl_wait = ', expl_wait, '\nimpl_wait = ', impl_wait)
    wd.get(url)
    wait.until(EC.title_contains('HP LP3065'))


    request.addfinalizer(wd.close)
    return wd, wait


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

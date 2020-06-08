from selenium import webdriver
import pytest
from page_objects.AdminLoginPage import AdminLoginPage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
from page_objects import MyListener
import logging


def pytest_addoption(parser):
    parser.addoption('--url', '-U', default='http://localhost')
    parser.addoption('--browser', '-B', choices=['Chrome', 'Firefox'], default='Chrome')
    parser.addoption('--expl_wait', '-E', type=int, required=None, default=0, help='explicit wait in seconds')
    parser.addoption('--impl_wait', '-I', type=int, required=None, help='explicit wait in seconds')
    parser.addoption('--file', '-F', type=str, required=None, help='logfile path/name')


# logging.basicConfig(level=logging.INFO, filename='selenium.log')
def pytest_configure(config):
    file_name = config.getoption('--file')
    return logging.basicConfig(level=logging.INFO, filename=file_name)


@pytest.fixture
def browser_params(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    else:
        wd = webdriver.Firefox()
    wd.get(url)

    # wd.implicitly_wait(20)
    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def browser_product(request):
    browser = request.config.getoption('--browser')
    expl_wait = request.config.getoption('--expl_wait')
    impl_wait = request.config.getoption('--impl_wait')

    url = 'http://localhost/index.php?route=product/product&path=18&product_id=47'
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    else:
        wd = webdriver.Firefox()
    wait = WebDriverWait(wd, expl_wait)
    if impl_wait:
        wd.implicitly_wait(impl_wait)
    print('\nexpl_wait = ', expl_wait, '\nimpl_wait = ', impl_wait)
    wd.get(url)
    wait.until(EC.title_contains('HP LP3065'))

    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd, wait


@pytest.fixture
def browser_catalogue(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/index.php?route=product/category&path=20_27'
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    else:
        wd = webdriver.Firefox()
    wd.get(url)

    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def browser_admin_login(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/admin/'
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    else:
        wd = webdriver.Firefox()
    wd.get(url)

    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def browser_search(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/index.php?route=product/search'
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    else:
        wd = webdriver.Firefox()
    wd.get(url)

    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def admin_page_fixture(request):
    browser = request.config.getoption('--browser')
    url = 'http://localhost/admin/'
    if browser == 'Chrome':
        test_name = request.node.name
        logger = logging.getLogger('chrome_fixture')
        logger.info('Started test "{}"'.format(test_name))
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
        # wd = webdriver.Chrome()
    else:
        wd = webdriver.Firefox()
    wd.get(url)

    username = wd.find_element(*AdminLoginPage.USERNAME)
    username.send_keys('user')
    password = wd.find_element(*AdminLoginPage.PASSWORD)
    password.send_keys('bitnami1')
    wd.find_element(*AdminLoginPage.LOGIN_BTN).click()
    try:
        wd.find_element_by_id("details-button").click()
        wd.find_element_by_id("proceed-link").click()
    except NoSuchElementException:
        print("FF doesn't get this window")
    # Alert(wd).accept()
    finally:
        wait = WebDriverWait(wd, 10)
        el = wait.until(EC.presence_of_element_located((By.ID, 'navigation')))
        print(el)

    wd.find_element_by_id('menu-catalog').click()
    products = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Products')))
    products.click()

    def fin():
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.fixture
def browser_with_listener(request):
    url = request.config.getoption('--url')
    test_name = request.node.name
    logger = logging.getLogger('chrome_fixture')
    logger.info('Started test "{}"'.format(test_name))
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    wd = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
    wd.get(url)

    # wd.implicitly_wait(20)
    def fin():
        browser = wd.get_log('browser')
        for l in browser:
            logger.warning(l)
        wd.close()
        logger.info('Chrome browser closed')
        logger.info('Test "{}" finished'.format(test_name))

    request.addfinalizer(fin)
    return wd

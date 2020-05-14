from locators import AdminPanelPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from time import sleep
from random import randint


def test_add_product(admin_page_fixture):
    wd = admin_page_fixture
    wait = WebDriverWait(wd, 5)
    actions = ActionChains(wd)
    add_button = wd.find_element(*AdminPanelPage.ADD_NEW_BTN)
    actions.move_to_element(add_button).click().perform()
    wait.until(EC.presence_of_element_located((*AdminPanelPage.PRODUCT_NAME_INPUT,)))
    wd.find_element(*AdminPanelPage.PRODUCT_NAME_INPUT).send_keys('new_product1')
    wd.find_element(*AdminPanelPage.META_TAG_INPUT).send_keys('new_product1')
    wd.find_element(*AdminPanelPage.DATA_TAB).click()
    wd.find_element(*AdminPanelPage.MODEL_INPUT).send_keys('new_model1')
    wd.find_element(*AdminPanelPage.SAVE_BTN).click()
    wait.until(EC.presence_of_element_located((*AdminPanelPage.SUCCESS_ALERT,)))
    sleep(3)


def test_mod_product(admin_page_fixture):
    wd = admin_page_fixture
    wait = WebDriverWait(wd, 5)
    wd.find_element(*AdminPanelPage.EDIT_BTN).click()
    wd.find_element(*AdminPanelPage.DATA_TAB).click()
    wd.find_element(*AdminPanelPage.INPUT_PRICE).clear()
    wd.find_element(*AdminPanelPage.INPUT_PRICE).send_keys(randint(10, 15000))
    sleep(3)
    wd.find_element(*AdminPanelPage.SAVE_BTN).click()
    wait.until(EC.presence_of_element_located((*AdminPanelPage.SUCCESS_ALERT,)))
    # sleep(3)


# '''
def products_amount(wd):
    table_body = wd.find_element(*AdminPanelPage.TABLE)
    products_qty = int(table_body.get_attribute('childElementCount'))
    return products_qty


def test_delete_product(admin_page_fixture):
    wd = admin_page_fixture
    products_qty = products_amount(wd)
    if products_qty == 20:
        try:
            wd.find_element(*AdminPanelPage.NEXT_PAGE).click()
            products_qty = products_amount(wd)
            print(products_qty)
        except NoSuchElementException:
            print('\nEXACTLY 20 ITEMS -> no pagination!')
    print(products_qty)
    last_item = wd.find_elements(*AdminPanelPage.CHECKBOX)[-1]
    last_item.click()
    wd.find_element(*AdminPanelPage.DELETE_BTN).click()
    Alert(wd).accept()
    sleep(3)
    if products_qty == 1:
        print('\nDELETING LAST ITEM!')
    else:
        assert products_amount(wd) == products_qty - 1
# '''

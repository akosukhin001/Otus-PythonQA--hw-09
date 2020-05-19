from page_objects import AdminPanelPage
from selenium.webdriver.common.alert import Alert
from time import sleep
from random import randint


# '''
def test_add_product(admin_page_fixture):
    AdminPanelPage(admin_page_fixture).click_add_new_button()
    AdminPanelPage(admin_page_fixture).wait_for_product_name_input()
    AdminPanelPage(admin_page_fixture).input_product_name('new_product1')
    AdminPanelPage(admin_page_fixture).input_meta_tag('new_product1')
    AdminPanelPage(admin_page_fixture).click_data_tab()
    AdminPanelPage(admin_page_fixture).input_model('new_model1')
    AdminPanelPage(admin_page_fixture).click_save_button()
    AdminPanelPage(admin_page_fixture).wait_for_success_alert()
    sleep(3)


def test_mod_product(admin_page_fixture):
    AdminPanelPage(admin_page_fixture).click_edit_button()
    AdminPanelPage(admin_page_fixture).click_data_tab()
    AdminPanelPage(admin_page_fixture).input_price(randint(10, 15000))
    AdminPanelPage(admin_page_fixture).click_save_button()
    AdminPanelPage(admin_page_fixture).wait_for_success_alert()
    sleep(3)


# '''

def test_delete_product(admin_page_fixture):
    wd = admin_page_fixture
    products_qty = AdminPanelPage(admin_page_fixture).products_amount()
    if products_qty == 20:
        if AdminPanelPage(admin_page_fixture).check_page_pagination():
            AdminPanelPage(admin_page_fixture).click_next_page()
            products_qty = AdminPanelPage(admin_page_fixture).products_amount()
            print(products_qty)
    print(products_qty)
    AdminPanelPage(admin_page_fixture).click_last_element()
    AdminPanelPage(admin_page_fixture).click_delete_button()
    Alert(wd).accept()
    sleep(3)
    if products_qty == 1:
        print('\nDELETING LAST ITEM!')
    else:
        assert AdminPanelPage(admin_page_fixture).products_amount() == products_qty - 1
# '''

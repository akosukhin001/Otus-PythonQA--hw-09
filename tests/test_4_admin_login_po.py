from page_objects import AdminLoginPage
from time import sleep


def test_title(browser_admin_login):
    assert browser_admin_login.title == AdminLoginPage(browser_admin_login).check_title()


def test_panel_text(browser_admin_login):
    text = AdminLoginPage(browser_admin_login).check_panel_text()
    assert text == 'Please enter your login details.'


def test_input_username(browser_admin_login):
    AdminLoginPage(browser_admin_login).input_username('admin')


def test_input_password(browser_admin_login):
    AdminLoginPage(browser_admin_login).input_password('bitnami1')


def test_login_button(browser_admin_login):
    AdminLoginPage(browser_admin_login).click_login_button()


def test_forgotten_password(browser_admin_login):
    AdminLoginPage(browser_admin_login).click_forgotten_password()


def test_login_all(browser_admin_login):
    admin_login = AdminLoginPage(browser_admin_login)
    admin_login.input_username('user')
    admin_login.input_password('bitnami1')
    admin_login.click_login_button()
    sleep(3)

from locators import AdminLoginPage
from selenium.webdriver.common.by import By
from time import sleep


def test_title(browser_admin_login):
    assert browser_admin_login.title == AdminLoginPage.TITLE


def test_panel_text(browser_admin_login):
    text = browser_admin_login.find_element_by_css_selector(AdminLoginPage.PANEL_TEXT).text
    assert text == 'Please enter your login details.'


def test_username(browser_admin_login):
    username = browser_admin_login.find_element_by_css_selector(AdminLoginPage.USERNAME)
    username.send_keys('admin')
    username.clear()


def test_password(browser_admin_login):
    password = browser_admin_login.find_element_by_css_selector(AdminLoginPage.PASSWORD)
    password.send_keys('bitnami1')
    password.clear()


def test_login_button(browser_admin_login):
    browser_admin_login.find_element_by_css_selector(AdminLoginPage.LOGIN_BTN).click()


def test_forgotten_password(browser_admin_login):
    browser_admin_login.find_element_by_css_selector(AdminLoginPage.FORGOTTEN_PASSWORD).click()


def test_login_all(browser_admin_login):
    test_username(browser_admin_login)
    test_password(browser_admin_login)
    test_login_button(browser_admin_login)
    sleep(5)
    # assert browser_admin_login.title == 'Dashboard'

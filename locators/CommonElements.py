from selenium.webdriver.common.by import By

css = By.CSS_SELECTOR
link_text = By.LINK_TEXT


class CommonElements:
    CART = (css, '#cart-total')
    NAV_LINKS = (css, 'ul.nav > li')
    SEARCH = (css, '[name=search]')
    CURRENCY = (css, '#form-currency')

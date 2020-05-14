from .CommonElements import CommonElements
from .CommonElements import css


class ProductPage(CommonElements):
    CART = (css, '#cart-total')
    CART_STATUS = (css, '.text-center')
    ALERT_MESSAGE = (css, '.alert')
    WISH_LIST_BTN = (css, '[data-original-title="Add to Wish List"]')
    COMPARE_BTN = (css, '[data-original-title="Compare this Product"]')
    PRODUCT_DETAILS = (css, 'ul.nav.nav-tabs > li')
    DELIVERY_DATE = (css, 'button.btn.btn-default > i.fa.fa-calendar')
    PRODUCT_QTY = (css, '#input-quantity')
    ADD_TO_CART_BTN = (css, '#button-cart')

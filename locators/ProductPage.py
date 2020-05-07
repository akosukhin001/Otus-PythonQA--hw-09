from .CommonElements import CommonElements

class ProductPage(CommonElements):
    CART = '#cart-total'
    WISH_LIST_BTN = '[data-original-title="Add to Wish List"]'
    COMPARE_BTN = '[data-original-title="Compare this Product"]'
    PRODUCT_DETAILS = 'ul.nav.nav-tabs > li'
    DELIVERY_DATE = 'button.btn.btn-default > i.fa.fa-calendar'
    PRODUCT_QTY = '#input-quantity'
    ADD_TO_CART_BTN = '#button-cart'

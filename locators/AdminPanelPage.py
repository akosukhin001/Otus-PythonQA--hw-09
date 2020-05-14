from .CommonElements import css
from .CommonElements import link_text


class AdminPanelPage():
    ADD_NEW_BTN = (css, '.fa-plus')
    COPY_BTN = (css, '.fa-copy')
    DELETE_BTN = (css, '.btn-danger')
    PRODUCT_NAME_INPUT = (css, '#input-name1')
    META_TAG_INPUT = (css, '#input-meta-title1')
    DATA_TAB = (link_text, 'Data')
    MODEL_INPUT = (css, '#input-model')
    SAVE_BTN = (css, '.fa-save')
    SUCCESS_ALERT = (css, '.alert-success')
    EDIT_BTN = (css, '[data-original-title="Edit"]')
    INPUT_PRICE = (css, '#input-price')
    CHECKBOX = (css, '[name="selected[]"]')
    TABLE = (css, 'tbody')
    NEXT_PAGE = (link_text, '>')

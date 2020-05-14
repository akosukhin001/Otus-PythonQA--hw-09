from .CommonElements import CommonElements
from .CommonElements import css


class SearchPage(CommonElements):
    KEYWORDS = (css, '#input-search')
    ALL_CATEGORIES = (css, 'select[name="category_id"]')
    IN_DESCR_CHECKBOX = (css, '#description')
    IN_SUBCAT_CHECKBOX = (css, '[name=sub_category]')
    SEARCH_BTN = (css, '#button-search')

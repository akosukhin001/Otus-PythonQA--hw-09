from .CommonElements import CommonElements

class SearchPage(CommonElements):
    KEYWORDS = '#input-search'
    ALL_CATEGORIES = 'select[name="category_id"]'
    IN_DESCR_CHECKBOX = '#description'
    IN_SUBCAT_CHECKBOX = '[name=sub_category]'
    SEARCH_BTN = '#button-search'

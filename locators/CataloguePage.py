from .CommonElements import CommonElements
from .CommonElements import css


class CataloguePage(CommonElements):
    FEATURED = (css, 'div.row .product-layout')
    ITEMS_LIST = (css, '#column-left > .list-group')
    LIST_VIEW_BTN = (css, '#list-view')
    GRID_VIEW_BTN = (css, '#grid-view')
    SORT_SELECT = (css, '#input-sort')
    SHOW_QTY_SELECT = (css, '#input-limit')

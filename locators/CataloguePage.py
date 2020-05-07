from .CommonElements import CommonElements


class CataloguePage(CommonElements):
    FEATURED = 'div.row .product-layout'
    ITEMS_LIST = '#column-left > .list-group'
    LIST_VIEW_BTN = '#list-view'
    GRID_VIEW_BTN = '#grid-view'
    SORT_SELECT = '#input-sort'
    SHOW_QTY_SELECT = '#input-limit'

from .CommonElements import CommonElements
from .CommonElements import css


class MainPage(CommonElements):
    FEATURED = (css, 'div.row .product-layout')
    PROMOBLOCK = (css, '#slideshow0')
    PROMOPAGINATOR = (css, '.swiper-pagination.slideshow0')
    ADV = (css, '#carousel0')
    ADVPAGINATOR = (css, '.swiper-pagination.carousel0')

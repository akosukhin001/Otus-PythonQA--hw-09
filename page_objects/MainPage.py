from selenium.webdriver.common.by import By
from page_objects import BasePage


class MainPage(BasePage):
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT

    FEATURED = (css, 'div.row .product-layout')
    PROMOBLOCK = (css, '#slideshow0')
    PROMOPAGINATOR = (css, '.swiper-pagination.slideshow0')
    ADV = (css, '#carousel0')
    ADVPAGINATOR = (css, '.swiper-pagination.carousel0')

    def find_featured(self, index):
        # print('\nself.logger=', self.logger)
        # print('\ntype(self)=', type(self))
        self.logger.info('find_featured')
        return self._get_element_text(self.FEATURED, index)

    def click_promoblock(self):
        self.logger.info('click_promoblock')
        self._click(self.PROMOBLOCK)
        return self

    def find_promopaginator(self):
        self.logger.info('find_promopaginator')
        return self._element(self.PROMOPAGINATOR)

    def find_adverb(self):
        self.logger.info('find_adverb')
        return self._element(self.ADV)

    def find_advpaginator(self):
        self.logger.info('find_advpaginator')
        return self._element(self.ADVPAGINATOR)

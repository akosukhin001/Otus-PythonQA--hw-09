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
        return self._get_element_text(self.FEATURED, index)

    def click_promoblock(self):
        self._click(self.PROMOBLOCK)
        return self

    def find_promopaginator(self):
        return self._element(self.PROMOPAGINATOR)

    def find_adverb(self):
        return self._element(self.ADV)

    def find_advpaginator(self):
        return self._element(self.ADVPAGINATOR)

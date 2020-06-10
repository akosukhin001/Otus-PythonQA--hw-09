import logging
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver


class MyListener(AbstractEventListener):
    # logging.basicConfig(level=logging.INFO, filename='selenium.log')
    logger = logging.getLogger('driver')


    def before_navigate_to(self, url, driver):
        self.logger.info(f'Navigating to "{url}"')

    def after_navigate_to(self, url, driver):
        self.logger.info(f'Navigated to "{url}"')

    def before_find(self, by, value, driver):
        self.logger.info(f'Searching for "{value}" by "{by}"')

    def after_find(self, by, value, driver):
        self.logger.info(f'Found "{value}" by "{by}"')

    def before_click(self, element, driver):
        self.logger.info(f'Clicking "{element}"')

    def after_click(self, element, driver):
        self.logger.info(f'"{element}" clicked')

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        pass

    def before_execute_script(self, script, driver):
        self.logger.info(f'Executing "{script}"')

    def after_execute_script(self, script, driver):
        self.logger.info(f'"{script}" executed')

    def before_close(self, driver):
        self.logger.info(f'closing - teardown')

    def after_close(self, driver):
        self.logger.info(f'closed - teardown')

    def before_quit(self, driver):
        self.logger.info(f'quiting')

    def after_quit(self, driver):
        self.logger.info(f'GoodBye')

    def on_exception(self, exception, driver):
        self.logger.error(f' raised {exception}')
        driver.save_screenshot(f'{exception}.png')

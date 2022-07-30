from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage (BasePage):

    HOME_PAGE_HEADER = (By.CSS_SELECTOR, 'a.blockbestsellers')
    USER_NAME = (By.CSS_SELECTOR, '.account > span:nth-child(1)')
    PHONE_ICON = (By.CSS_SELECTOR, '.shop-phone > i:nth-child(1)')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.PHONE_ICON)

    def get_header_value(self):
        if self.is_visible(self.HOME_PAGE_HEADER):
            return self.get_element_text(self.HOME_PAGE_HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.USER_NAME):
            return self.get_element_text(self.USER_NAME)

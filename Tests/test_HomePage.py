from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_user_name(self):
        self.LoginPage = LoginPage(self.driver)
        home_page = self.LoginPage.do_login(TestData.EMAIL, TestData.PASSWORD)
        user_name = home_page.get_account_name_value()
        assert user_name == TestData.USER_NAME

    def test_home_page_title(self):
        home_page = HomePage(self.driver)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        home_page = HomePage(self.driver)
        header = home_page.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_settings_icon(self):
        home_page = HomePage(self.driver)
        assert home_page.is_setting_icon_exist()

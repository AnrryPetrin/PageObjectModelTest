from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    """By locators - OR"""
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    LOGIN_BUTTON = (By.ID, 'SubmitLogin')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot your password?')

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_URL)

    '''Page Actions for Login Page'''

    '''this is used to get the page title'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    '''this is used to check forgot password link'''
    def is_forgot_password_link_exist(self):
        return self.is_visible(self.FORGOT_PASSWORD_LINK)
    '''this is used to login to app'''
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

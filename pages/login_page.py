from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'You are not at LOGIN page'

    def should_be_login_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.Login_link
            ).is_displayed(), 'No Login form at this page...'

    def should_be_register_form(self):
        assert self.browser.find_element(
            *LoginPageLocators.Registration_link_email
            ).is_displayed(), 'No Registration form at this page...'

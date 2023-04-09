from selenium.webdriver.common.by import By
import re

from fixture.locators import SignupLocators as locator


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        self.app.session.navigate_to_page(self.app.base_url + "/signup_page.php")
        self.app.session.change_field_value(locator.username, username)
        self.app.session.change_field_value(locator.email, email)
        self.app.session.click(locator.signup_button)

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        # TBD: to check this
        if mail is None:
            raise FileExistsError
        url = self.extract_confirmation_url(mail)

        self.app.session.navigate_to_page(url)
        self.app.session.change_field_value(locator.password, password)
        self.app.session.change_field_value(locator.password_confirm, password)
        self.app.session.click(locator.update_user_button)

    def extract_confirmation_url(self, text):
        # $ for end of line  < MULTILINE option
        return re.search("http://.*$", text, re.MULTILINE).group(0)

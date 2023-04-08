from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fixture.locators import LoginLocators as locator, ProjectLocators as project_locator


class SessionHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.home_page = base_url
        self.manage_project_page = "/mantisbt-1.2.20/manage_proj_page.php"
        self.manage_page = "/mantisbt-1.2.20/manage_overview_page.php"

    def login(self, username, password):
        wd = self.app.wd
        # self.open_home_page()
        self.navigate_to_page(self.home_page)
        self.change_field_value(locator.username, username)
        self.change_field_value(locator.password, password)
        wd.find_element(By.CSS_SELECTOR, locator.login).click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, locator.logout)) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, locator.logged_user).text

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, locator.logout).click()
        # wd.find_element(By.NAME, locator.username)

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.home_page)

    def open_manage_page(self):
        wd = self.app.wd
        if self.is_on_page(self.manage_page) is False:
            self.click(project_locator.manage_link)

    def open_manage_project_page(self):
        wd = self.app.wd
        if self.is_on_page(self.manage_project_page) is False:
            self.click(project_locator.manage_project_link)

    def navigate_to_page(self, link):
        wd = self.app.wd
        if self.is_on_page(link) is False:
            wd.get(link)

    def click(self, locator):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, locator).click()

    def change_field_value(self, locator, value):
        wd = self.app.wd
        if value is not None:
            input_element = wd.find_element(By.CSS_SELECTOR, locator)
            input_element.click()
            input_element.clear()
            input_element.send_keys(value)

    def change_dropdown_value(self, locator, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element(By.CSS_SELECTOR, locator)).select_by_visible_text(value)

    def is_on_page(self, url):
        wd = self.app.wd
        return wd.current_url.endswith(url)

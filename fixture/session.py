from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.home_page = base_url

    def login(self, username, password):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.NAME, "username").click()
        wd.find_element(By.NAME, "username").clear()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "password").click()
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.find_element(By.NAME, "username")

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.home_page)

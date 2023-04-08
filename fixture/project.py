from selenium.webdriver.common.by import By

from fixture.locators import ProjectLocators as locator
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def fill_form(self, project):
        self.app.session.change_field_value(locator.project_name, project.name)
        self.app.session.change_dropdown_value(locator.status_dropdown, project.status)
        if project.is_inherit is False:
            self.app.session.click(locator.is_inherit_checkbox)
        self.app.session.change_dropdown_value(locator.view_status_dropdown, project.view_status)
        self.app.session.change_field_value(locator.description, project.description)

    def create(self, project):
        # navigate to Manage Projects page
        self.app.session.open_manage_project_page()
        # press Create New Project button
        self.app.session.click(locator.create_new_project_button)
        self.fill_form(project)
        # press Add Project button
        self.app.session.click(locator.add_project_button)
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.session.open_manage_page()
            self.app.session.open_manage_project_page()
            self.project_cache = []
            for row in wd.find_elements(By.XPATH, locator.project_row):
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.TAG_NAME, "a").get_attribute("href").split("=")[-1]
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_status = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(id=id, name=name, status=status, view_status=view_status,
                                                  description=description))
        return list(self.project_cache)

    def make_project_name_unique(self, project, project_list):
        names = self.get_project_names(project_list)
        while project.name in names:
            project.name += "1"

    def get_project_names(self, project_list):
        return [p.name for p in project_list]

    def get_first_name(self, project_list):
        names = self.get_project_names(project_list)
        return names[0]
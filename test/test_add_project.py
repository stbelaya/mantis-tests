from selenium.webdriver.common.by import By

from fixture.generation import random_string
from model.project import Project
from fixture.locators import ProjectLocators as locator


def test_add_project(app):
    old_projects = app.soap.get_project_list()
    project = Project(name=random_string("name_", 15), status="stable", view_status="private",
                      description=random_string("description_", 20))
    app.project.make_project_name_unique(project, old_projects)
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_add_project_duplicate_name(app):
    projects = app.soap.get_project_list()
    if not projects:
        project = Project(name=random_string("name_", 15), status="stable", view_status="private",
                          description=random_string("description_", 20))
        app.project.create(project)
        projects = app.soap.get_project_list()
    project = Project(name=app.project.get_first_name(projects), status="stable", view_status="private",
                      description=random_string("description_", 20))
    app.project.create(project)
    error = app.wd.find_element(By.CSS_SELECTOR, locator.app_error_duplicate_name).text
    assert error == "APPLICATION ERROR #701"

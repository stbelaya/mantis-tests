from selenium.webdriver.common.by import By

from model.project import Project
from fixture.locators import ProjectLocators as locator


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name="sw00 name", status="stable", view_status="private",
                      description=" sw00 description very good project")
    app.project.make_project_name_unique(project, old_projects)
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_add_project_duplicate_name(app):
    projects = app.project.get_project_list()
    if not projects:
        project = Project(name="sw00 name", status="stable", view_status="private",
                          description=" sw00 description very good project")
        app.project.create(project)
        projects = app.project.get_project_list()
    project = Project(name=app.project.get_first_name(projects), status="stable", view_status="private",
                      description=" sw00 description very good project")
    app.project.create(project)
    error = app.wd.find_element(By.CSS_SELECTOR, locator.app_error_duplicate_name).text
    assert error == "APPLICATION ERROR #701"

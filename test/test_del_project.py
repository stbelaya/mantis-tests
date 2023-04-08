import random

from model.project import Project


def test_delete_some_project(app):
    app.session.ensure_login("administrator", "root")
    old_projects = app.project.get_project_list()
    if not old_projects:
        app.project.create(name="sw00 name")
        old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

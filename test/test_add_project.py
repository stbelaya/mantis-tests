from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name="sw00 name", status="stable", view_status="private",
                      description=" sw00 description very good project")
    app.project.prepare_project_data(project, old_projects)
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

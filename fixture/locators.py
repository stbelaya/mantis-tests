from selenium.webdriver.common.by import By


class LoginLocators:
    username = '[name="username"]'
    password = '[name="password"]'
    login = "input[value='Login']"
    logout = "Logout"
    logged_user = "td.login-info-left span"


class ProjectLocators:
    manage_link = 'a[href="/mantisbt-1.2.20/manage_overview_page.php"]'
    manage_project_link = 'a[href="/mantisbt-1.2.20/manage_proj_page.php"]'

    create_new_project_button = 'input[value="Create New Project"]'

    # Add Project form fields
    project_name = '[name="name"]'
    is_inherit_checkbox = '[name="inherit_global"]'
    status_dropdown = '[name="status"]'
    view_status_dropdown = '[name="view_state"]'
    description = '[name="description"]'

    add_project_button = 'input[value="Add Project"]'

    # Projects table
    project_row = "//table[3]/*/tr[@class='row-1' or @class='row-2']"

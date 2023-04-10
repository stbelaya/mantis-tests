from selenium.webdriver.common.by import By


class LoginLocators:
    username = '[name="username"]'
    password = '[name="password"]'
    login = "input[value='Login']"
    logout = "Logout"
    logged_user = "td.login-info-left span"


class SignupLocators:
    username = '[name="username"]'
    email = '[name="email"]'
    signup_button = 'input[value="Signup"]'
    password = '[name="password"]'
    password_confirm = '[name="password_confirm"]'
    update_user_button = 'input[value="Update User"]'


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

    # Project dictionaries
    status = ["development", "release", "stable", "obsolete"]
    is_inherit = [True, False]
    view_status = ["public", "private"]

    # Projects table
    project_row = "//table[3]/*/tr[@class='row-1' or @class='row-2']"
    name_cell = ()

    # Edit Project form fields
    delete_project_button = 'input[value="Delete Project"]'

    # confirmation screen
    delete_project_sure = 'input[value="Delete Project"]'

    app_error_duplicate_name = 'td.form-title'


class SoapLinks:
    mantisconnect_wdsl = "http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl"

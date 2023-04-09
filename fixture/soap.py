from suds.client import Client
from suds import WebFault
import json


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config["webadmin"]["username"]
        password = self.app.config["webadmin"]["password"]
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            project_data = client.service.mc_projects_get_user_accessible(username, password)
            # TBD: need to parse this json
            data = json.load(project_data)
            return data
        except WebFault:
            return []
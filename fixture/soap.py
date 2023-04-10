from suds.client import Client
from suds import WebFault
import xmltodict

from model.project import Project
from fixture.locators import SoapLinks as links


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(links.mantisconnect_wdsl)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config["webadmin"]["username"]
        password = self.app.config["webadmin"]["password"]
        client = Client(links.mantisconnect_wdsl, retxml=True)
        try:
            raw_data = client.service.mc_projects_get_user_accessible(username, password)
            project_list = self.parse_project_list(raw_data)
            return project_list
        except WebFault as wf:
            print(f"Error {wf} during SOAP response receiving is occurred")
            return []

    def parse_project_list(self, raw_data):
        project_list = []
        parsed = xmltodict.parse(raw_data, xml_attribs=False)
        data = [dict(d) for d in parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']
        ['ns1:mc_projects_get_user_accessibleResponse']['return']['item']]
        for p in data:
            project = Project(id=p["id"], name=p["name"], status=p["status"]["name"],
                              view_status=p["view_state"]["name"], description=p["description"])
            project_list.append(project)
        return project_list

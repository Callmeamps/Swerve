import os
import anvil.server
import config
from team_members import jennifer_hancock
from toolboxes.basictools import BasicTools

anvil_server = os.environ["ANVIL_SERVER_UPLINK"]

anvil.server.connect(anvil_server)

all_agents = anvil.server.call("get_agents").search()

def get_project_update(agent_name):
    agent = anvil.server.call("get_agent_details", agent_name)
    agent_projects = agent["projects"]
    projects = []
    for project in agent_projects:
        project_name = project["title"]
        project_title = project["project_id"]
        project_summary = project["summary"]
        status = anvil.server.call("get_project_status", project_title)
        project_update = BasicTools.update_user_on_projects(agent_id=agent_name, projects=projects, status=status)
        project_details = {"project_name": project_name, "project_summary": project_summary, "project_status": status, "project_update": project_update}
        projects.append(project_details)
    print(projects)

for agent in all_agents:
    get_project_update(agent["id_name"])
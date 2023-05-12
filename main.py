import os
import anvil.server
import config
from team_members import jennifer_hancock

anvil_server = os.environ["ANVIL_SERVER_UPLINK"]

anvil.server.connect(anvil_server)

all_agents = anvil.server.call('get_agents').search()

if all_agents:
    for agent in all_agents:
        print(agent)

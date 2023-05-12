import os
import anvil.server

anvil_server = os.environ["ANVIL_SERVER_UPLINK"]

anvil.server.connect(anvil_server)


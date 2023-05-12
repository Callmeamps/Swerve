from langchain.agents.tools import Tool
import agent_user
from address import Address
from toolboxes.copywriter_tools import CustomCopy
from toolboxes.basictools import BasicTools

jennifers_address = Address(
    country="ZA",
    state="MP",
    city="Emalahleni",
    street="Jenny's Drive",
    stand="1",
    zip_code="1042"
)

jennifers_tools = [
    Tool(
    name="Write Post",
    func=CustomCopy.write_post,
    description="Save writing to Markdown."
    ),
    Tool(
    name="Update Client",
    func=BasicTools.update_user_on_projects,
    description="When you need to update a client on the current status of a project."
    )
]

jennifer_hancock = agent_user.AutoAgent(
    first="Jennifer",
    last="Hancock",
    dob="01/15/1990",
    email="jenny_hancock@outlook.com",
    phone="0716716699",
    address=jennifers_address,
    role="Agent",
    salary="100000",
    project=[],
    tools=jennifers_tools
)

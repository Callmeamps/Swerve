import agent_user
from address import Address

jennifers_address = Address(
    country="ZA",
    state="MP",
    city="Emalahleni",
    street="Jenny's Drive",
    stand="1",
    zip_code="1042"
)

jennifer_hancock = agent_user.AutoAgent(
    first="Jennifer",
    last="Hancock",
    dob="01/15/1990",
    email="jenny_hancock@outlook.com",
    phone="0716716699",
    address=jennifers_address,
    role="Agent",
    salary="100000",
    project="",
    tools=[]
)

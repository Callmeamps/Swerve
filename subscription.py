import datetime
from project import Project
from client import Client

today = datetime.date.today()

class Subscribe:
    def __init__(self, client, project, subscription_date=today):
        self.subscription_date = subscription_date

        if isinstance(client, Client):
            self.client = client
        else:
            raise ValueError("Invalid Client...")
        
        if isinstance(project, Project):
            self.project = project
        else:
            raise ValueError("Invalid Project...")
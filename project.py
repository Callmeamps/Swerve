import os
import datetime
from supabase import create_client, Client
from delivareable import Deliverable

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

today = datetime.date.today()

class Project:
    def __init__(self, name, description, notes, budget, deliverable, due_date, start_date=today, internal_project=False):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.notes = notes
        self.budget = budget
        self.internal_project = internal_project
        self.deliverables = []

        if isinstance(deliverable, Deliverable):
            self.deliverables.append(deliverable)
        elif isinstance(deliverable, list):
            for item in deliverable:
                if isinstance(item, Deliverable):
                    self.deliverables.append(item)
                else:
                    raise TypeError("Invalid Deliverable type")
    def save_project(self):
        data = supabase.table('Projects').insert({"id": 1, "title": self.name, "summary": self.description, "notes": self.notes, "budget": self.budget, "internal_project": self.internal_project, "deliverables": self.deliverables, "start_date": self.start_date, "due_date": self.due_date}).execute()
        
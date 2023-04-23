import datetime
from delivareable import Deliverable

today = datetime.date.today()

class Project:
    def __init__(self, name, description, notes, budget, deliverable, due_date, start_date=today):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.notes = notes
        self.budget = budget
        self.deliverables = []

        if isinstance(deliverable, Deliverable):
            self.deliverables.append(deliverable)
        elif isinstance(deliverable, list):
            for item in deliverable:
                if isinstance(item, Deliverable):
                    self.deliverables.append(item)
                else:
                    raise TypeError("Invalid Deliverable type")

        
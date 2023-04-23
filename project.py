import datetime

class Project:
    def __init__(self, name, description, start_date, due_date, notes, budget, delivareables):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.due_date = due_date
        self.notes = notes
        self.budget = budget
        self.delivareables = []

        
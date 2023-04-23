from person import Person
from project import Project

class TeamMember(Person):
    def __init__(self, first, last, dob, email, phone, address, role, salary, project):
        super().__init__(first, last, dob, email, phone, address)
        self.role = role
        self.salary = salary
        self.projects = []

        if isinstance(project, Project):
            self.projects.append(project)
        elif isinstance(project, list):
            for job in project:
                if not isinstance(job, Project):
                    raise TypeError("Invalid Project...")
                self.projects.append(job)
    
    


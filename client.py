from person import Person
from company import Company

class Client(Person):
    def __init__(self, first, last, dob, email, phone, address, position, company, international=False):
        super().__init__(first, last, dob, email, phone, address)
        self.international = international
        self.position = position
        self.companies = []

        if isinstance(company, Company):
            self.companies.append(company)
        elif isinstance(company, list):
            for entry in company:
                if not isinstance(entry, Company):
                    raise TypeError("Invalid Company...")

            self.companies = company

    def add_company(self, company):
        if not isinstance(company, Company):
            raise TypeError("Invalid Company...")
        self.companies.append(company)

    def is_subscribed(self, subscribed):
        return False
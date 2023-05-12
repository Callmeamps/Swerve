import os
from supabase import create_client, Client
import datetime
from person import Person
from company import Company
from subscription import Subscribe

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class Client(Person):
    def __init__(self, first, last, dob, email, phone, address, position, company, subscribed=False, international=False):
        super().__init__(first, last, dob, email, phone, address)
        self.name = f"{first} {last}"
        self.international = international
        self.position = position
        self.subscribed = subscribed
        self.companies = []
        if isinstance(company, Company):
            self.companies.append(company)
        elif isinstance(company, list):
            for entry in company:
                if not isinstance(entry, Company):
                    raise TypeError("Invalid Company...")

            self.companies = company

    def register_subscription(self, password="admin"):
        res = supabase.auth.sign_up({
        "email": self.email,
        "password": password,
          "options": {
                "data": {
                "first_name": self.name,
                "date_of_birth": self.dob,
                }
            }
        })
        print(f"Registered Successfully: {res}")
        self.subscribed = True
        return self.subscribed

    def add_company(self, company):
        if not isinstance(company, Company):
            raise TypeError("Invalid Company...")
        self.companies.append(company)

    def is_subscribed(self):
        if self.subscribed is True:
            print(f"{self.name} is subscribed")
            return True
        return False

    
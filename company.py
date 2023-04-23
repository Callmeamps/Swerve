from address import Address

class Company:
    def __init__(self, name, founded, founder, contact_number, address):
        self.company_name = name
        self.date_founded = founded
        self.contact_number = contact_number
        self.addresses = [] 
        self.founders = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise TypeError("Invalid Address...")
            self.addresses = address

        else:
            raise TypeError("Invalid Address...")

        if isinstance(founder, str):
            self.founders.append(founder)
        elif isinstance(founder, list):
            for entry in founder:
                if not isinstance(entry, str):
                    raise TypeError("Invalid Founder...")
            self.founders = founder

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address...")
        self.addresses.append(address)
    
    def remove_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address...")
        self.addresses.remove(address)

    def add_founder(self, founder):
        if not isinstance(founder, str):
            raise TypeError("Invalid Founder...")
        self.founders.append(founder)
    
    def remove_founder(self, founder):
        if not isinstance(founder, str):
            raise TypeError("Invalid Founder...")
        self.founders.remove(founder)

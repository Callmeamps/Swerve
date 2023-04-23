from address import Address

class Person:
    def __init__(self, first, last, dob, email, phone, address):
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.email = email
        self.phone = phone
        self.addresses = []

        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise TypeError("Invalid Address...")
            
            self.addresses = address
        else:
            raise TypeError("Invalid Address...")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address...")
        self.addresses.append(address)
    
    def remove_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address...")
        self.addresses.remove(address)
        
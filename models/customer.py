class Customer:

    def __init__(self, id, name, address, email="", password=""):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.address = address
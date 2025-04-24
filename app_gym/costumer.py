class Costumer:
    def __init__(self, id = None, first_name = None, last_name = None, membership = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership

    def __str__(self):
        return f"Id: {self.id}, First name: {self.first_name}, Last name: {self.last_name}, Membership: {self.membership}"
    
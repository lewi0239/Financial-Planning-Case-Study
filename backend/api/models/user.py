

class User:
    def __init__(self, email: str, password: str, account_name: str):
        self.email = email
        self.password = password
        self.account_name = account_name
        self.advisor_link = advisor_link()

        def advisor_link(Retail, Advisor):
            # Search for User from Database
            # Send a advisor_link request


class Retail(User):
    # Inherit from the parent class User
    def __init__(self, email, password, account_name, advisor_link):
        super().__init__(email, password, account_name, advisor_link)


class Advisor(User):
    # Inherit from the parent class User
    def __init__(self, email, password, account_name, advisor_link):
        super().__init__(email, password, account_name, advisor_link)

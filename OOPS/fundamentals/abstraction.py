from abc import abc, abstractmethod


class Individual(abc):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_access(self):
        pass


class Admin(Individual):
    def __init__(self, username):
        super().__init__(username)

    def get_access(self):
        return ["Change Password"]


class User(Individual):
    def __init__(self, username):
        super().__init__(username)

    def get_access(self):
        return ["View Password"]


admin = Admin("admin")
user = User("user")
print(admin.get_access())
print(user.get_access())

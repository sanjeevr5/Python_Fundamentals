# Encapsulation is part of data hiding
# Helps to reveal the private information only when needed and does not allow unauthorized access to the private data.
# Encapsulation generally uses the getter and setter pattern.


class Bank:
    def __init__(self, initial_deposit):
        self.__balance = initial_deposit

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.__balance -= amount


b1 = Bank(1000)
print(b1.get_balance())
try:
    print(b1.__balance)
except AttributeError as e:
    print(e)
b1.deposit(500)
print(b1.get_balance())
b1.withdraw(200)
print(b1.get_balance())
# In Python we can still access the private variable by using the _<class_name>__<variable_name> syntax
print(b1._Bank__balance)

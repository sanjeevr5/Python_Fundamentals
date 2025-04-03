#Single Responsibility Principle
#A class should have only one reason to change, meaning that a class should have only one job.

#Our Invoice class has multiple responsibilities like calculating the invoice, printing the invoice, and saving the invoice.
#We can refactor the Invoice class to separate these responsibilities into different classes.
class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")

class Invoice:
    def __init__(self, vehicle: Vehicle, quantity : int, tax: int):
        self.vehicle = vehicle
        self.quantity = quantity
        self.tax = tax
        self.total = 0
    
    def calculate_invoice(self):
        self.total = (self.vehicle.price * self.quantity) + (self.tax * self.quantity)
        return self.total

class InvoicePrinter:
    def __init__(self, invoice : Invoice):
        self.invoice = invoice
    
    def print_invoice(self):
        print(f"Vehicle: {self.invoice.vehicle.brand} {self.invoice.vehicle.model}\nPrice: {self.invoice.price}")

class SavePrinter:
    def __init__(self, invoice : Invoice):
        self.invoice = invoice
    
    def save_invoice(self):
        print(f"Saving invoice for {self.invoice.vehicle.brand} {self.invoice.vehicle.model}")

vehicle = Vehicle("Toyota", "Corolla", 2019, 20000)
invoice = Invoice(vehicle, 2, 1000)
printer = InvoicePrinter(invoice)
saver = SavePrinter(invoice)


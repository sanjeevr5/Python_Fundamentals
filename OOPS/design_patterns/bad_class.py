class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started")

class Invoice:
    def __init__(self, vehicle: Vehicle, price : float, quantity : int, tax: int, total: int):
        self.vehicle = vehicle
        self.price = price
        self.quantity = quantity
        self.tax = tax
        self.total = total
    
    def calculate_invoice(self):
        self.total = (self.price * self.quantity) + self.tax
        return self.total
    
    def print_invoice(self):
        print(f"Vehicle: {self.vehicle.brand} {self.vehicle.model}\nPrice: {self.price}")
    
    def save_invoice(self):
        print(f"Saving invoice for {self.vehicle.brand} {self.vehicle.model}")

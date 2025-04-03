from typing import Union


class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")


class Car(Vehicle):
    def __init__(self, name, color, model):
        self.vehicle = Vehicle(name, color)
        self.model = model

    def start(self):  # Overriding the start method of the parent class
        self.vehicle.start()
        print(f"{self.vehicle.name} {self.model} started")

    def stop(self):  # Overriding the stop method of the parent class
        self.vehicle.stop()
        print(f"{self.vehicle.name} {self.model} stopped")

    def registration_number(
        self, ip: Union[str, int]
    ):  # Polymorphism - Method overloading (Duck typing in Python)
        if isinstance(ip, int):
            ip = str(ip)
        print(f"Registration number is {'IND ' + ip}")


car = Car("Toyota", "Red", "Corolla")
car.start()
car.stop()
car.registration_number(1000)
car.registration_number("ABC")

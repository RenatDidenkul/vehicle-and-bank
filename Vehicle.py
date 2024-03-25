class Vehicle:
    def __init__(self, make, model, year):
        self.make = "Plastic"
        self.model = "Toyota"
        self.year = "2000"
       
class Car:
    def __init__(self):
        self.color = "Yellow"
        self.mode = "Pagani"
        self.num_doors = "550"

class Motorcycle:
    def __init__(self):
        self.color = "Gray"
        self.mode = "Tamiya"
        self.engine_size = "300"
       
vehicle = Vehicle("Plastic", "Toyota", "2000")
car = Car()
print(car.color, car.mode, car.num_doors)
motorcycle = Motorcycle()
print(motorcycle.color, motorcycle.mode, motorcycle.engine_size)
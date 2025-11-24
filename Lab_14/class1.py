class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_details(self):
        return f"Car: {self.brand}, Model: {self.model}"
    
my_car = Car("Toyota", "Corolla")
print(my_car.car_details())  
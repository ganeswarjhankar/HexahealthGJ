#######The car class##########

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
###fuel capacity and level in galons
        self.fuel_capacity=50
        self.fuel_level = 0

    def fill_tank(self):
        """to full capacity"""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")
    def drive(self):
        print("The car is moving")
"""Creating an object froom class Car"""
my_car =Car("audi","audiModel",2023)

"""assessing attribute values"""
print(my_car.make)
print(my_car.model)
print(my_car.year)
"""calling Methods"""
my_car.fill_tank()
my_car.drive()


"""Create multiple objects"""

my_bike = Car("bicycle","bicycle2.0",2023)


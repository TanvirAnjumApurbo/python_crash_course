from car import ElectricCar
from car import Car
from car import Car, ElectricCar  # Import multiple classes from a module.
import car  # Import the entire module.
from car import *  # Import all classes from a module.
from car import Car as C  # Import a class with an alias.
import car as c  # Import a module with an alias.


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


my_mustang = car.Car('ford', 'mustang', 2020)
print(my_mustang.get_descriptive_name())

# Importing car class to the module
from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = Car('voltswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#import entire module and use dot notation to access specific classes
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


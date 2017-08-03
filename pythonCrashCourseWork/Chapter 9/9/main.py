#Chapter 9 ex 9 date : 02/07/17.

#Imports
from cars import ElectricCar,Battery

#Variables

#Objects 
my_car = ElectricCar("Tesla","Roadster",2008,Battery())
my_battery = my_car.battery

#Functions

#Body
my_battery.get_range()
my_battery.upgrade_battery()
my_battery.get_range()
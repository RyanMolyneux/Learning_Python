#Chapter 8 ex 15 date : 25/06/17.

#Imports
import printing_functions

#Variables
my_car = {}

#Functions


#Body

my_car = printing_functions.make_car("tesla","roadster",engine_type="electric",car_type="sports",tesla_founder="eberhard")
print("My New Car & Some Extra Information\n-----------------------------------------\n")

for key,value in my_car.items():
	print("\n\n",key.upper()," : ",value.title())
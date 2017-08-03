#Chapter 8 ex 14 date : 22/06/17.

#Variables

#Function
def make_car(manufacturer,model,**other):
	"""Demonstrate how to create optional values simply using dictionary."""
	car = {"Car Manufacturer" : manufacturer,"Car Model" : model}

	for key,value in other.items():
		car[key] = value

	return car
#Body
my_car = make_car("Tesla motors","Roadster",engine_type = "Electric")
print("My New Cars information\n------------------\n")

for key,value in my_car.items():
	print(key," : ",value)
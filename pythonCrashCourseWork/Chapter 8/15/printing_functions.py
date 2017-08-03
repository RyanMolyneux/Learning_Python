#Functions
def make_car(manufacturer,model,**other):
	"""Demonstrates how to create optional dictionary values in function."""
	car = {"Car manufacturer" : manufacturer,"Car model" : model}
	
	for key,value in other.items():
		car[key] = value
	return car
#Chapter 8 ex 5 date : 20/06/17.

#Variables
country = ""
city = ""


#Functions

def describe_city(city,country = "Ireland"):
	"""This function accepts & displays both country & city as parameter that it describes"""
	print("\n\nA Great city in ",country," is ",city,".")

#Body

print("\n---------------------------------\n\tCity Descriptor\n---------------------------------\n"
     +"\n\nExample\n-------------")
describe_city("Dublin")

while(True):

	print("\n\nEnter country in which the city is based.")
	country = input("\n\ninput : ")
	print("\n\nPlease now enter city name")
	city = input("\n\ninput : ")

	if(country == "exit") or (city == "exit"):
		print("\n\nYou have chosen to exit goodbye hopefully see you soon.")
		break
	else:
		describe_city(city,country)



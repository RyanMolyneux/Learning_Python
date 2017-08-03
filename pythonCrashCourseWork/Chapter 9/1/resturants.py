#Chapter 9 ex 1 date : 26/06/17.

#Classes
class Resturant():
	"""Simple Demonration of conventional styling of a class."""

	#Constructor
	def __init__(self,resturant_name,cuisine_type):
		#Attributes instantiation
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type

	#Methods
	
	def describe_resturant(self):
		print("\n\nInformation about :",self.resturant_name," \n---------------------------------\n"
		     +"\n\nCuisine type : ",self.cuisine_type)

	def open_resturant(self):
		print("\n\n",self.resturant_name.title()," is open!!! :') .")
	



#Classes
class Resturant():
	"""Simple Demonration of conventional styling of a class."""

	#Constructor
	def __init__(self,resturant_name,cuisine_type,number_served=0):
		#Attributes instantiation
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	#Methods
	
	def describe_resturant(self):
		print("\n\nInformation about :",self.resturant_name," \n---------------------------------\n"
		     +"\n\nCuisine type : ",self.cuisine_type,"\nNumber of customers served : ",str(self.number_served))

	def open_resturant(self):
		print("\n\n",self.resturant_name.title()," is open!!! :') .")

	def set_served(self,new_serves):
		"""Used to set value of number of customers served."""
		self.number_served = new_serves

	def increment_served(self,new_serves):
		"""Used to increment current value of number of serves."""
		self.number_served += new_serves
			
































	


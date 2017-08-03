#Classes

class Resturant():
	"""Demonstration of use of classes"""

	#Constructor
	def __init__(self,name,cuisine):
		"""Demonstration of use of constructor in python."""
		#Attributes
		self.name = name
		self.cuisine = cuisine

	#Methods

	def describe_resturant(self):
		"""Call this method to show information about the method."""
		print("\n\n",self.name.title()," Information\n--------------------------------\nCuisine type : ",self.cuisine)

	def open_resturant(self):
		"""Call this to show customers that resturant is open."""
		print("\n\n",self.name," is now open :D.")
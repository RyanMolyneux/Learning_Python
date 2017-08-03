#Classes
class Resturant():
	"""Simple Demonstration of conventional styling of a class."""

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





class IceCreamStand(Resturant):
	"""Ice cream stand is a class which inherits from resturant."""

	#Constructor
	def __init__(self,resturant_name,cuisine_type,*flavours):
		"""Constructor used to create & initialise attibutes of class ice cream stand & its parent class."""
		super().__init__(resturant_name,cuisine_type)
		self.flavours = flavours

	#Methods
	def display_flavours(self):
		"""Method used to display all flavours of ice cream to customer."""

		print("Ice Cream Flavours\n--------------------------\n")
		for flavour in self.flavours:
			print("\nFlavour : ",flavour)


		
		



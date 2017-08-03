#Classes
class Resturant():

	#Constructor
	def __init__(self,name,cuisine,owner):
		"""Used to define & initialise attributes of this class."""
		self.name = name
		self.cuisine = cuisine
		self.owner = owner		

	#Methods
	def describe_resturant(self):
		"""Method displays information about the resturant."""
		print("\n",self.name.title()," Resturant\n-------------------------\n\n Owner : ",self.owner,"\n\n Cuisine : ",self.cuisine)

	def open_resturant(self):
		"""Method for displaying an indication to wether or not resturant is open or closed."""
		print("\n---------------------------\n",self.name.title()," Now Open.\n----------------------------\n")
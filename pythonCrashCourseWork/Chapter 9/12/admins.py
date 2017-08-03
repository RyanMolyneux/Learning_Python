
#Imports
from users import User
#Classes
class Admin(User):
	"""Specific type of user with special privileges."""

	#Constructor
	def __init__(self,first_name,last_name,age,email,pet_name,password,priveledges):
		super().__init__(first_name,last_name,age,email,pet_name,password)
		self.priveledges = priveledges

	#Methods
	def check_priveledges(self):
		"""Used to simple display the priveledges this admin currently has over the system."""
		print("\n--------------------------\nAdmin Priveledges\n---------------------------\n\n")
		for priveledge,access in self.priveledges.items():
			print("\n",priveledge," : ",access)

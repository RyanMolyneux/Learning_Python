#Classes

class User():
	"""Class for creating user accounts."""
	
	#Constructor
	def __init__(self,first_name,last_name,age,email,pet_name,password):
		"""Constructor for user class."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.pet_name = pet_name
		self.password = password

	#Methods
	def describe_user(self):
		"""Used to display information about users account pet_name&password&email are left out for security reasons."""
		print("\n\nAbout ",self.first_name+" "+self.last_name,"\n---------------------------------------\n"
		     +"Age : ",self.age,"\n\n")	

	def greet_user(self,user):
		"""Method used to send greeting to user."""
		print("\n\nHello there ",user.first_name,"\nSent From : ",self.first_name+" "+self.last_name)

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

	






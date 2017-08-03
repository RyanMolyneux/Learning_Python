#Classes

class User():
	"""Class for creating user accounts."""
	
	#Constructor
	def __init__(self,first_name,last_name,age,email,pet_name,password,login_attempts=0):
		"""Constructor for user class."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.pet_name = pet_name
		self.password = password
		self.login_attempts = login_attempts

	#Methods
	def describe_user(self):
		"""Used to display information about users account pet_name&password&email are left out for security reasons."""
		print("\n\nAbout ",self.first_name+" "+self.last_name,"\n---------------------------------------\n"
		     +"Age : ",self.age,"\n\n")	


	def greet_user(self,user):
		"""Method used to send greeting to user."""
		print("\n\nHello there ",user.first_name,"\nSent From : ",self.first_name+" "+self.last_name)

	def increment_attempts(self):
		"""Used to increment current value of login attempts"""
		self.login_attempts += 1

	def reset_attempts(self):
		"""Used to reset value of login attempts to 0. """
		self.login_attempts = 0


		

"""This will be there starting point of this program from here al other code will execute."""
#Chapter 10 ex 13 DATE : 18/07/18.

#Imports
import json

#Variables
file = "username.json"


#Objects - EMPTY

#Functions

def greet_user():
	"""This function is used to provide the appropriate greeting to users."""
	if get_stored_user_name():
		with open(file) as userFile:
			user_name = json.load(userFile)
		print("\n\nIs this your user name : ",user_name)

		if input("\nYes or No\nInput : ").lower() == "yes":
			print("\n\nWelcome back ",user_name)
		else:
			print("\n\nWe will remember you ",get_new_user_name())
	else:
		print("\n\nWe will remember you ",get_new_user_name())

def get_stored_user_name():
	"""Used to retrieve user name fro users file."""
	try:
		with open(file) as userFile:
			user_name = json.load(userFile)
		
	except FileNotFoundError:
		return None
	else:
		return user_name

def get_new_user_name():
	"""Used for the user to enter his/her username so it ma be stoed for later use."""
	#Tried w+ with json does not work so to seperate openings for file needed.
	with open(file, "w") as userFile:
		json.dump(input("\n\nPlease enter your name \nInput : "),userFile)
	with open(file) as userFile:
		return json.load(userFile)

#Body
greet_user()

	




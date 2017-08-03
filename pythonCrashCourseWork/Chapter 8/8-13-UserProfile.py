#Chapter 8 ex 13 date: 22/06/17

#Variables
my_profile = {}
#Functions
def make_profile(first,last,**profile):
	"""Used for demonstration purposes of Arbitrary values."""
	user_profile = {"Name" : first+" "+last,}
	for key,value in profile.items():
		user_profile[key] = value
	return user_profile
#Body
print("\n\nThank you for registering\n--------------------------\nUser Details\n---------")
my_profile = make_profile("ryan","m",DOB = "8/8/18")

for key,value in my_profile.items():
	print(key," : ",value)
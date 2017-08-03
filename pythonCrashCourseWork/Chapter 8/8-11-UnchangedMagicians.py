#Chapter 8 ex 11 date : 21/06/17.

#Variables
magicians = ["Bonnie","Jules","Sam"]
#Functions
def make_great(magicians):
	"""Used for list modification"""
	#Local Variable
	index = 0

	while index < len(magicians):
		magicians[index]+=" is a great magician."
		index+=1
	return magicians

def show_magicians(magicians):
	"""Passes a list to te function then prints it."""
	for magician in magicians:
		print(magician)

#Body
print("\nGreat Magicians\n--------------------\n")

show_magicians(make_great(magicians[:]))

print("\nOrigionals\n-------------------\n")
show_magicians(magicians)
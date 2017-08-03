"""Used to store & display your favourite number."""
#Chapter 10 ex 12 DATE : 17/07/17.

#Import 
import json

#Variables
file = "favourite_number.txt"
favourite_num = 0

#Objects - EMPTY

#Functions
def store_num():
	"""Simple function used to store your favourite number."""
	num = input("\n\nPlease enter your favourite number : ")

	with open(file, "w") as fileObject:
		json.dump(num,fileObject)

def read_num():
	"""Simple function used to read in & display your favourit number."""
	try:	
		with open(file) as fileObject:
			num = json.load(fileObject)	
	except FileNotFoundError:
		return None
	else:
		return num

#Body

favourite_num = read_num()
if favourite_num:
	print("Your favourite number is ",favourite_num)
else:
	store_num()
	print("We will remember that for you")
"""Simple program used to read in your favourite number & display it to the screen."""
#Import
import json

#Variables
file = "favourite_number.txt"

#Objects - EMPTY
#Functions - EMPTY

#Body

with open(file) as fileObject:
	print("\n\nFavourite Number is : ",json.load(fileObject))	
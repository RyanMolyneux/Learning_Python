"""Simple program used to ask user for favourite number & store it in a file."""
#Chapter 10 ex 11 DATE : 17/07/18.
#Imports
import json

#Variables
file = "favourite_number.txt"
favourite_number = 0

#Objects - EMPTY
#Functions - EMPTY

#Body

favourite_number = input("\n\nPlease enter your favourite number : ")

with open(file, "w") as fileObject:
	json.dump(favourite_number,fileObject)
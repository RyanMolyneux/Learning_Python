"""This will be a basic program which just consists of code counting the number of times 'the' appears in a text file."""
#Chapter 10 ex 10 DATE:17/07/18.

#Import - EMPTY

#Variables 
file_name = ""
text = ""

#Objects - EMPTY
#Functions - EMPTY

#Body

file_name = input("\n\nPlease enter name of the file & rember extensions.\nInput : ")

with open(file_name) as fileObject:
	text = fileObject.read()

print("\n\nThe number times 'the' has been used in ",file_name," is ",str(text.lower().count("the")))	
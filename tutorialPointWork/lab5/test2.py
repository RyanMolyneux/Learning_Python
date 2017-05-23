#In this session we will be working with strings and how to access values from them.

print("\nTEST-1\n----------------------------\n");

"""Today we will test out how to create substrings, which will involve slicing
of an existing string."""

#Variables
variable_string = "Pycon"

variable_substring = variable_string[2:-1]

#Note minus 1 is a short hand index for the end of the string.

if(len(variable_string) == len(variable_substring)):
	print("\n\n'variable substring' is not a substring of 'variable_string'");
else:
	print("\n\nvariable substring is a stubstring of variable string.");

print("\nTEST-2\n------------------------------\n");

#Updating String
"""This is better well known as concatinating to a string two ways of doing this
are during print or as assignment , assignment is some what permanant as long as
you do not reinitialise the string but print is not permenant as soon as you exit
the print method that concatinated value is gone."""


variable_string_permanent = variable_string +" is On!!!.";

print("\n\nPrint using temporary concatination : ",variable_string+" is On!!!");

print("\n\nPrint using permenant re assignment : ",variable_string_permanent);
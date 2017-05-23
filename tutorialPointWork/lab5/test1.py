"""Today we  are going over different typpes of numbers in python such as int/
Integer,long also known as long integer these are both known as whole numbers
then their is the real numbers such as pythons float & complex."""

print("\nTEST-1\n-------------------------");

#Whole Numbers
	#My int.
variable_integer = 10

	#My long int

variable_long = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

#Real Numbers

	#My floating point number

variable_float = 1000.00

	#My Complex number

variable_complex = 2.14j

print("\n\nINT : ",variable_integer,"\n\nLONG : ",variable_long,"\n\nFLOAT : ",variable_float,"\n\nCOMPLEX : ",variable_complex);

"""Something to note with 'long integers' is that in the  newer versions of Python
the uppercase 'L' at the end of the value is no longer needed to specify it as
a Long integer it is now done implcitly."""

print("\nTEST-2\n-------------------------------------\n");

"""Now we are going to test conversion of these variables from one type to the next
it is never really needed to be done specifically by the user but in certain cases
it is."""

print("Number Conversion\n-------------");

#variable_integer = float(variable_integer)

#variable_long = complex(variable_long)

#variable_float = int(variable_float)


print("\n\nInt converted to float : ",variable_integer,"""
\n\nLong converted to complex : """,variable_long,"""
\n\nFloat converted to integer""",variable_float);

"""Note that complex numbers cannot be converted to integer or float types."""


print("\nTEST-3\n-----------------------\n");


"""In this Section we will cover some important mathmatical functions that are
predefined for use in Python such as 'abs' which is used to return the absolute
value of the number passed in,'ceil' which is used to round number to the higher whole number
,'pow' which is used to result of value to the power of
value & 'random' which is used to generate a random number."""

import math,random

#Notice all values are being assigned to seperate values on the same line this
#can be short hand way and neat way of value assignment.
variable_integer_minus,variable_float,variable_integer_random = -100,3.32,int(variable_float*random.random())


print("""\nAbsolute Function Result : """,abs(variable_integer_minus),"""\n\n
Rounded Function Result : """,math.ceil(variable_float),"""\n\nPower of Function :""",pow(variable_float,2),"""
\n\nRandom Function Result : """,variable_integer_random);




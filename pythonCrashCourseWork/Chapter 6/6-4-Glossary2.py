#Chapter 6 ex 4 date : 13/06/17.

#Variables
programming_terms = {"variable" : "Name given for a space in memory  for easy access variables can be of varying data types.",
		     "integer" : "Whole number value which only stores  values before the decimal point.",
		     "float" : "Real numbers which as opposed to whole numbers stores values given past the decimal point.",
		     "string" : "Strings are made up of stream of characters which is just text based value.",
		     "list" : "It is as its name says a list, but the key thing about is its a data type which can store multiple different datatypes all at once in python lists are dynamic which means they can grow in size.",
		     "tuple" : "Very similar to the list but what is key about this data type is once values have been set they can be added or removed but they cannot be edited.",
		    }
#Main Body
print("\n\nProgramming Terminology\n-------------------------\n")
for word,definition in programming_terms.items():
	print("\n",word.title(),"\nDEFINITION : ",definition)
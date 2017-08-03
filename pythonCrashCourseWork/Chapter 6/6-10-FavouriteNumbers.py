#Chapter 6 ex 10 date : 14/06/17.
#Variables
	#Dictionaries
people_favouriteNumbers = {"ken" : list(range(0,30,4)),
			     "josh" : list(range(4,43,5)),
			     "cali" : list(range(2,52,3)),
			     "kala" : list(range(47,79,9)),
			    }
#Main Body
print("\nFavourite Numbers Survey Results\n------------------------------------\n")
for key in people_favouriteNumbers:
	print("\n",key.title()," : ",people_favouriteNumbers[key])
print("\n------------------------------------")
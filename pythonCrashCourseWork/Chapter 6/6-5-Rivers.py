#Chapter 6 ex 5 date : 13/06/17.

#Variables
rivers_countries = {"nile" : "eygpt",
		    "amazon" : "south america",
		    "mississippi" : "america",
		    "yangtze" : "china",
		    "congo" : "chambeshi",
		    }


#Main Body

print("\nLarge Rivers & Countries they are situated\n-----------------------------------\n\n")
for river in rivers_countries.keys():
	print("\nThe River : ",river," is situated in : ",rivers_countries[river],"\n")

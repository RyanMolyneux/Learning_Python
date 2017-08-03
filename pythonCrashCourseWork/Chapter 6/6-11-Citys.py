#Chapter 6 ex 11 date : 14/06/17.
#Variables
	#Dictionaries
cities = {"Dublin" : {"country" : "ireland","population" : "1.345 million","fact" : "dublin is the capital city of ireland."},
	  "London" : {"country" : "england","population" : "8.674 million","fact" : "london is the largest city in the united kingdom."},
	  "Rome" : {"country" : "italy","population" : "2.877 million","fact" : "rome was founded in 753 bc by romulus."},
	 }
#Main Body

print("\nCities & A bit about them\n-----------------------------\n")
for city,info, in cities.items():
	print("\t\t",city.upper(),"\n------------------------------------\n")
	for key,value in info.items():
		print("\n",key.upper()," : ",value.title())
	print("\n------------------------------------\n")
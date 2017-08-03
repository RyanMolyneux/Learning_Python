#Chapter 6 ex 9 date : 14/06/17.

#Variables
NYC = {"friends" : ["james","derek","jane"],
       "attraction" : "statue of liberty",
       "common weather" : "mild heat",
	}
Tokoyo = {"friends" : ["derek","jamie","jules","samantha"],
	 "attraction" : "roppongi",
	 "common weather" : "hot",
	 }
Egypt = {"friends" : ["keith","shane"],
	 "attraction" : "pyramids",
	 "common weather" : "very hot",
	}

favourite_places= [NYC,Tokoyo,Egypt]
#Main Body
print("\nSome of my friends favourite places\n---------------------------\n")
for place in favourite_places:
	print("\n---------------------------\n")
	for key, value in place.items():
		print("\n",key.upper()," : ",value)
	print("\n---------------------------")
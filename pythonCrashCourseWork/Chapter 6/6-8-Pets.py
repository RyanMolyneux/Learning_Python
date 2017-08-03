#Chapter 6 ex 8 date : 14/06/17.

#Variables
	#Dictionaries
moly = {"type" : "dog", 
	"owner" : "julia",
	}

milky = {"type" : "cat", 
	 "owner" : "jameson",
	}

quorks = {"type" : "ferret",
	  "owner" : "nickelson",
	 }
temie = {"type" : "buggie",
	 "owner" : "sam",
	}
jack = {"type" : "parrot",
	"owner" : "brian",
	}

milly = {"type" : "mouse",
	 "owner" : "santenika",
	}
	#Lists
pets = [moly,milky,quorks,temie,jack,milly]


#Main Body

print("\nMy Friends Pets\n-------------------------\n")
for pet in pets:
	print("\n-------------------------\n")
	for key, value in pet.items():
		print("\n",key.upper()," : ",value.title())
	print("\n\n-------------------------\n\n") 
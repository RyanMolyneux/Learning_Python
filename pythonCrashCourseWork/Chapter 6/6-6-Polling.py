#Chapter 6 ex 6 date : 13/06/17.

#Variables
language_polls = {"Jennifer" : "Fortran" ,
		  "Jane Doe" : "Coebol" ,
		  "Sam Pratt" : "C"  ,
		  "James Dunne" : "Java" ,
		  "June Dale": "C#",
		  }
missing_polls = ["Keith Helkum","Joe Bloggs","James Dunne"]


#Main Body
print("\nFav Language Missing Polls\n---------------------\n")
for name in missing_polls:
	if name not in language_polls.keys():
		print("\n\n",name," We would like you to take our quick pole please.")
	else: 
		print("\n\n",name," Thank you for participating in our pole.")
#Chapter 6 ex 7 date : 13/06/17.

#Variables
friend_1 = {"first name" : "Toelad",
	    "last name" : "Jamax",
	    "DOB" : "13/06/1997",
	   }
friend_2 = {"first name" : "James",
	    "last name" : "Blues",
	    "DOB" : "14/07/1996"
	   }
friend_3 = {"first name" : "Timmy",
	    "last name" : "Turnip",
	    "DOB" : "15/08/1995",
	   }
friend_4 = {"first name" : "Jules",
	    "last name" : "DEcoda",
	    "DOB" : "16/09/1994",
	   }

friends_list = [friend_1,friend_2,friend_3,friend_4]

#Main Body
print("\n\nFriend List \n------------------------------\n")
for friend in friends_list:
	print("\n-------------------------------")
	for key,value in friend.items():
		print("\n",key," : ",value)
	print("\n-------------------------------")
		
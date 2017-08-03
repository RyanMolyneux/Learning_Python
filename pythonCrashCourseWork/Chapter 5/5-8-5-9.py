#Chapter 5 ex 8 date : 11/06/17.

#Variables
user_list = ["admin","ryan","jim","tim","paul"]
temp_user = "admin"


#This is a poor patch of code but it is more for demonstration purposes.

if(user_list):

	for user in user_list:
		if(temp_user == user) and (temp_user == "admin"):
			print("\n\nHello Admin would you like status report.")
		elif(temp_user == user):
			print("Welcome back : ",user)
		else:
			print("\n\nIm sorry but it seems that this account does not  exist.")
else:
	print("\n\nIt Seems that no users currently exist we must add some.")
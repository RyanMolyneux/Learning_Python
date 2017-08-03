#Chapter 5 ex 10 date : 11/06/17.

#Variables
current_users = ["admin","john","tom","timmo","gypo"]
new_users = ["tom","admin","ryan","jupiter","jonno"]

#Main Body
for user in new_users:
	if(user in current_users):
		print("\n\nYou must enter a different username.",user)
	elif(user not in current_users):
		print("This username is available & has been added ",user,".")
		current_users.append(user)
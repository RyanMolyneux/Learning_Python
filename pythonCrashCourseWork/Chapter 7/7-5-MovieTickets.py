#Chapter 7 ex 5 date : 17/06/17.

#Variables
age = ""
flag = True
#Main Body

print("\n-------------------------------------\nSannuuuuusa CiNema Today\n-------------------------------------\n")
while (True):
	age = input("\n\nPlease enter your age : ")
	num_age = int(age)
	
	if(num_age < 3):
		print("\n\nYour ticket is freeeeee.")
	elif(num_age >= 3) and (num_age <= 12):
		print("\n\nYour ticket costs $10.")
	elif(num_age > 12 ):
		print("\n\nYour ticket costs $15.")
	

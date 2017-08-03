#Chapter 7 ex 6 date : 17/06/17.

#Variables
list_toppings = []
topping_input = ""
flag = True

#Main Body
print("\n\n--------------------------------\nDomanjoies how might we help you\n-------------------------------------\n")
while (True):

	topping_input = input("Please enter topping : ")

	if(topping_input !=  "q") and (topping_input != "quit"):
		list_toppings.append(topping_input)
	else:
		break
	
print("\n\nYour pizza\n------------------\n")
for topping in list_toppings:
	print("",topping) 
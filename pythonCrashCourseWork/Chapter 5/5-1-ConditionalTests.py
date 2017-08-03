#Chapter 5 ex 1 date : 11/06/17.

#Variables
pizza_ingredients = ["Tomato","Cheese","Dough","Toppings"]
email_addresses = ["rm@gmail.com","tim@gmail.com"]
email_passwords = ["password1","password2"]
age = 19
county = "Dublin"

#Main Body

#TEST1

#Better for checks in larger programs.
print("My age is 18?")
if(age == "18"):
	print("True")
else:
	print("False")

#TEST2

#Simpler way of getting answer.
print("My Age is 19?")
print(age==19)

#TEST3
print("\nMy of birth is not Dublin? ->",(county!="Dublin"))

#TEST4
print("\n\nMy county of birth Cork? -> ",(county=="Cork"))

#TEST5
temp_email = "Rm@gmail.com"
temp_password = "password1"

if(temp_email == email_addresses[0]) and (temp_password == email_passwords[0]):
	print("\n\nYou have successfully Signed in :)")
else:
	print("\n\nEither password OR email you have entered are incorrect.")

#TEST6
if(temp_email.lower() == email_addresses[0]) and (temp_password.lower() == email_passwords):
	print("\n\nWelcome back ",temp_email)
else:
	print("\n\nEither password OR email you've entered are incorrect.")

#TEST7
temp_email = "TIM@gmail.com"
if(temp_email.lower not in email_addresses):
	print("\n\nThis email is currently unassigned to an account please register.")
else:
	print("\n\nThis email is currently in use.")

#TEST8
temp_ingredient = "bbq sauce"
if(temp_ingredient in pizza_ingredients):
	print("\n\nThis is an ingredient of pizza.")
else:
	print("\n\nThis is not an ingredient of pizza.")

#TEST9
temp_ingredient = "Tomato"
if(temp_ingredient not in pizza_ingredients):
	print("\n\nThis is not an ingredient of pizza.")
else:
	print("\n\n",temp_ingredient," is an ingredient of pizza.")
#TEST10
temp_ingredient = "chocolate"
temp_ingredient2 = "tomatoes"
if(temp_ingredient in pizza_ingredients) or (temp_ingredient2 in pizza_ingredients):
	print("\n\n",temp_ingredient," or ",temp_ingredient2," are an ingredient in pizza.")
else : 
	print("\n\nNeiter are an ingredient in pizza.")

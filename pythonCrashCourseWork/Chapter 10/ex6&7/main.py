"""This is the main file which will be the starting point of control for this addition program."""
#Chapter 10 ex 6&7 DATE : 17/07/18.

#Imports
from functions import add_values

#Variables
num1 = 0
num2 = 0

#Functions 
def check_choice(num):
	if (num == "quit") or (num == "exit"):
		return True
	else:
		return False
	
#Objects - EMPTY

#Body
print("\n\n---------------------------------\nAddition Calculator\n---------------------------------\n")

while True:
	num1 = input("\n\nPlease enter first number : ")
	if check_choice(num1) == True:
		break
	num2 = input("\n\nPlease enter second number : ")
	if check_choice(num2) == True:
		break
	add_values(num1,num2)

print("\n\n---------------------------------\nThank you for using our app goodbye.\n---------------------------------\n")
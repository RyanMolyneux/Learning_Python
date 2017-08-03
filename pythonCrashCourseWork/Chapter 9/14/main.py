#Chapter 9 ex 14 date : 05/07/17.

#Imports
from random import randint

#Function
def roll_die(no_sides = 6):
	return str(randint(1,no_sides))

#Body
print("\n--------------------------------------------------\nWelcome To Die Rollers dont b a fool Roll & Rule.\n--------------------------------------------------\n")
while(True):
	typed = input("\n\nPlease enter number of sides : ")
	if(typed.lower() == "exit"):
		break
	print("\nSIDE : ",roll_die(int(typed)))
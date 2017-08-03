#Chapter 7 ex 3 date : 17/06/17.

#Variables
value_passed = 0

#Main Body
print("\n-------------------------------------\nWelcome to multiples 10\n-------------------------------------\n")

value_passed = int(input("\n\nPlease enter a value : "))

if(value_passed%10 == 0):
	print("\n\nYou speek the truth this sure is a multiple of 10.")
else:
	print("\n\n",value_passed," -> This is not a multiple of 10 you lier.")
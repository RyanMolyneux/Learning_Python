#Chapter 4 ex 10 date : 10/06/17.

#Variables
my_list = ["Ryan","M","Dublin","Ireland","19","11/03/99"]

#Entire List
print("\nEntire List\n-----------------------\n",my_list)

#Using slice
print("\nFirst three items of list\n-----------------------\n")
for value in my_list[:3]:
	print("\n",value)

print("\nThree items from the middle of the list\n-----------------------\n")
for value in my_list[2:5]:
	print("\n",value)

print("\nLast three items in list\n-----------------------\n")
for value in my_list[3:]:
	print("\n",value)

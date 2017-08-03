#Chapter 7 ex 2 date : 17/06/17.

#Variables
seating_number = 0

#Main Body

print("\n\n-------------------------------------\n\tPerlos Resturant\n-------------------------------------")

seating_number = int(input("\nHow many will be dinning with you today : "))

if(seating_number > 8):
	print("\n\nIm sorry but you will need to wait for a table to open up.")
else:
	print("\n\nThank you for dinning with us today now if we can lead you to your table.")

"""Various Functions stored here for different uses throughout programs runtime. """

#Functions
def add_values(num1,num2):
	"""This function is used in the case of addition of two values."""
	try:
		answer = int(num1)+int(num2)
	except ValueError:
		print("\n\nSorry but these two values cannot be added as 1 of them is not a type of number.")
	else:
		print("\n\n",num1," + ",num2," = ",str(answer))
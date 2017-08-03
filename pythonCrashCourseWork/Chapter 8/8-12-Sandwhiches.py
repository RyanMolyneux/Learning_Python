#Chapter 8 ex 12 date : 22/06/17.

#Variables
sandwhich = []
#Functions
def show_sandwhich(*ingredients):
	print("\n\nYour sandwich\n---------------")
	for ingredient in ingredients:
		print(">",ingredient.title())

#Body
print("\n--------------------------------\n\tSandwhich maker\n--------------------------------\n")
	
sandwhich_ingredient1 = input("\nPlease enter ingredient 1 : ")
sandwhich_ingredient2 = input("\nPlease enter ingredient 2 : ")
sandwhich_ingredient3 = input("\nPlease enter ingredient 3 : ")
sandwhich_ingredient4 = input("\nPlease enter ingredient 4 : ")
show_sandwhich(sandwhich_ingredient1,sandwhich_ingredient2,sandwhich_ingredient3,sandwhich_ingredient4)	
	
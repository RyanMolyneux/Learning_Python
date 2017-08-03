"""This module may consist of functions which run various tasks throughout the main program."""
#Functions
def display_animals(animal_list):
	for animal in animal_list:
		try:
			with open(animal) as animalObject:
				animal_names = animalObject.read()

		
		except FileNotFoundError:
			#EX 8 - print("\n\nSorry but one of the files entered cannot be located.")
			pass
		else:
			print("\n\n",animal_names)
			


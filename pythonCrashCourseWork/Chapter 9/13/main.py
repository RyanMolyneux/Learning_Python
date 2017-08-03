#Chapter 9 ex 13 date : 05/07/17.

#Imports
from collections import OrderedDict



#Functions
def fill_glossary():
	"""Used to create, fill & return dictionary."""
	glossary = OrderedDict()

	glossary["Malware"] = "Umbrella term for evil computer software such as viruses & worms."
	glossary["Object"] = "Objects are instances of classes that are created & filled with various information."
	glossary["Method"] = "Method is a special term given to a function that belongs to a specific class."

	return glossary
#Body
my_glossary = fill_glossary()

for key,value in my_glossary.items():
	print("\n",key.upper()," : ",value.title())
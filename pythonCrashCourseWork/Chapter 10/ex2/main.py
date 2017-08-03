#Chapter 10 ex 2 date : 06/07/17.

#Variables
file = "MyDocuments\python.txt"

#Body

with open(file) as file_content:
	file_text = file_content.read()
	print("\n-----------------------\nUnEdited text \n-----------------------\n\n",file_text.rstrip())
	file_text = file_text.replace("python","Java")
	print("\n----------------------------------------------\n Edited text what is changed ?\n-------------------------------------------\n",file_text)
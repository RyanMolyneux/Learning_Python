#Chapter 10 ex 1 date : 06/07/17.

#Variables

#Functions
def read_entirity(file):
	"""Used to read files contents all at once."""
	with open(file) as file_content:
		print(file_content.read().rstrip())

def read_lbl(file):
	"""Used as sort of a buffe for reading files content used when you more focus of files contents."""
	with open(file) as file_content:
		for line_text in file_content:
			print(line_text.rstrip())

def read_list(file):
	"""Used to read list that is created when using specific function provided by file io psl."""
	with open(file) as file_content:
		file_list = file_content.readlines()

	for text in file_list:
		print(text.rstrip())

#Body
file = input("\n Please input name of the file & dont forget the extension.\n\ninput :")

print("\n-----------------------\nFile Entirity reading\n-----------------------\n")
read_entirity(file)

print("\n\n-----------------------\nFile Line By Line reading.\n-----------------------\n")
read_lbl(file)

print("\n\n-----------------------\nFile List reading.\n-----------------------\n")
read_list(file)


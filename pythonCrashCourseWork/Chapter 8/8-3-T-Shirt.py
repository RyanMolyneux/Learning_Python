#Chapter 8 ex 3 date : 18/06/17.

#Variables
shirt_size = "large"
shirt_text = "Yeeeeeeeeessssssssssssssssssssss!!!"

#Functions
def make_shirt(shirt_size,shirt_text):
	"""Function used for creating new t-shirts of different sizes & designs"""
	print("\nT-Shirt Size : ",shirt_size,"\n\nShirt Text : ",shirt_text)	
#Body
print("\n-------------------------------------\n\t Shirt Maker\n-------------------------------------\n")
#Positional
make_shirt("small","Hmmmmmmm!!!")
#Keyword
make_shirt(shirt_text,shirt_size)
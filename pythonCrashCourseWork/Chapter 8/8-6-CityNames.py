#Chapter 8 ex 6 date : 21/06/17.

#Variables

#Functions

def city_country(country,city):
	"Used to Simply concatinate a pair of strings."
	text = country+", "+city
	return text

#Body

print("\n-------------------------------------\n\tString Converter\n-------------------------------------\n")

for index in range(0,3):
	print("Session : ",(index+1),"Complete\n--------------------------------------\n",city_country(input("\nPlease Enter Country : "),input("Please Enter City : ")))
	
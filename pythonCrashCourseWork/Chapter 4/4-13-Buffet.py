#Chapter 4 ex 13 date : 11/06/17.

#Variables
buffets_food = ("Chicken","Beef","Sausage","Chips","Egg")

print("\nBuffet Food\n---------------------------\n")
for food in buffets_food[:]:	
	print("\n",food)

#Intentional Error Code.
#buffets_food[0] = "Mince Meat"

#Revised Menu
buffets_food = ("Mince Meat","Fish","Chips","Sushi","Rice")

print("\nRevised Menu\n---------------------------\n")
for food in buffets_food[:]:
	print("\n",food) 
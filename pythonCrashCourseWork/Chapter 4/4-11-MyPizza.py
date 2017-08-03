#Chapter 4 ex 11 date : 10/06/17.

#Variables
my_pizzas = ["Margarita","Peparonie","Mixed Meat"]
friends_pizzas = my_pizzas[:]

print("\n\nMy favorite pizzas\n-----------------------------\n")
for value in my_pizzas[:]:
	print("\n",value)

print("\n\nFriends Favourite Pizzas\n----------------------------\n")
for value in friends_pizzas[:]:
	print("\n",value)

my_pizzas.append("Sausage & Bacon")
friends_pizzas.append("Pinapple")

print("\n\nMy favourites updated",my_pizzas)
print("\n\nFriends favourites",friends_pizzas)
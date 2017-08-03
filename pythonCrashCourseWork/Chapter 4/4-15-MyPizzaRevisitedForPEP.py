#Chapter 4 ex 15 date : 11/06/17.

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
print("\n\nMy favourites updated",my_pizzas)

friends_pizzas.append("Pinapple")
print("\n\nFriends favourites",friends_pizzas)
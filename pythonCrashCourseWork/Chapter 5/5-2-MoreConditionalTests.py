#Chapter 5 ex 2 date : 11/06/17.

#Variables
my_food = "Chicken Wrap"
my_shopping_tuple = ("Ham","Cheese","Chicken","Beef") 
my_shopping_tuple2 = ("Onion","Peper","Parsley")

#TEST - Equality&Inequality
print("\nAm i Eating Pizza ? Answer -> ",(my_food == "Pizza"))

print("\n\nAm i not Eating a Chicken Wrap ? Answer -> ",(my_food.lower() != "chicken wrap"))

#TEST - Numerically

print("\n\nIs 30 Equal to 20 ? Answer -> ",(30 == 20))

print("\n\nIs 40 not Equal to 4*10? Answer -> ",(40 != (4*10)))

print("\n\nIs 45 greater tyhan 37 ? Answer ",(45 > 37))

print("\n\nIs 5 less than or equal to 4",(5 <= 4))

print("\n\nIs yogurt on either of my shopping lists ? Answer -> ",("yogurt" in my_shopping_tuple or "yogurt" in my_shopping_tuple2))

#TEST - Lists


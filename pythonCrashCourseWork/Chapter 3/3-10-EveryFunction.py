#Chapter 3 ex 10 date : 10/06/17.

#Variables
#List Creation
my_list = ["Ryan M","Dublin","Ireland","19"]

#Accessing single value
print("Accessing Single Value\n---------------------\n",my_list[0])

#Accessing multiple values.
print("Accessing Multiple Values\n--------------------\n",my_list)

#Adding to list
my_list.append("Great Guy")
print("\nAppended List\n-----------------------\n",my_list)

#Inserting new values at any position
my_list.insert(1,"Adult")
print("\nList with new inserted value.\n------------------------\n",my_list)

#Editing Values of list Not really a function but accessing is
my_list[0] = "Bob M"
print("\n\nEdited List not really a function  but worth mention\n----------------------\n",my_list)


#Deleting values from list
del my_list[0]
print("\nList with values removed using 'del' \n------------------------------\n",my_list)

#Popping Values from list
print("\nValue removed from my list using 'pop'\n--------------------------\n",my_list.pop())

#Remove value removed using remove which comes in handy when you dont know index 
my_list.remove("Adult")
print("\n\nList Now after using remove\n--------------------------\n",my_list,"\n\nNote : this only removes single instance of that value.")

#List Sorted
print("\n\nSorted List temporarly with 'sorted'\n-------------------------\n",sorted(my_list))

#Reversing order of list
my_list.reverse()
print("\n\nList after its order has become reversed\n-------------------------\n",my_list)
my_list.reverse()

#List sort permanent
my_list.sort()
print("\n\nList after origional order has become permanently lost & is now sorted alphabetically\n--------------------------------\n",my_list[0:-1])


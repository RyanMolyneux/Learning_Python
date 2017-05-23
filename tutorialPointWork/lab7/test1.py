#Python functions

#Variables
variable_list = [1,2,3];
variable_list2 = ["Hello","Ryan"]

#Functions
	#PrintFunction
def myFunc(variable_list):
	"This is used to demonstrate how python functions work."
	for variable_int in variable_list :
		print("\n\nValue : ",variable_int);
	else:
		print("\n\nThere are no more values to be displayed.");	
	return;

	#refrence appending function.
def refrenceFunc(variable_list):
	"Used to demonstrate how to add to reference outside of function."
	variable_list.append(["GoodBye","Ryan"]);
	print("\n\nInside Function : ",variable_list);
	return;
	
	#Overiting reference function.
def overRefFunc(variable_list):
	"Used to demonstrate how refrences can also be overitten one passed in."
	variable_list = ["Go","Away","Ryan"];
	print("\n\nInside Function : ",variable_list);
	return;

"""Note this above function only overwrites the local variable list not the 
outter list."""


print("\n\n\tTEST-1\n------------------------\n");

print("\n\nNow we will cover functions in python defining them calling them and updating references vs overwriting.\n\n");

print("\tPrinting Function \n-------------------------------\n");
#calling function
myFunc(variable_list);


#Appending to list.
print("\n\tAppending to List \n-----------------------------------\n");
refrenceFunc(variable_list2);
print("\n\nOutside Function : ",variable_list2);


#Overwriting reference.
print("\n\tOverwriting Reference \n------------------------------------\n");
overRefFunc(variable_list2);
print("\n\nOutside Fucntion : ",variable_list2);

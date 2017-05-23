#Tonight we will be studying tuples to start

print("\nTEST - 1\n-------------------------\n");

"""To start todays lesson we will start with simple operations you can perform 
with tuples such as 'initialise','view','update','delete'."""

#Variables - Tuple initialization.
variable_tuple = (1,2,3);
variable_tuple2 = (4,5,"Six",7,8);
#Concat tuples
variable_tuple3 = variable_tuple+variable_tuple2;

#Tuple Viewing

print("\n\nView full contents of tuple by simply typing 'name'/'name[0:-1]' like so :",variable_tuple);

"""Note you cannot technically update contents of a tuple but you can concatinate 
them for a new tuple.""" 

print("\n\nThis is made from two different tuples which concatinated to create this one : ",variable_tuple3);

"""Now we are going to demonstrate how to 'del' tuple we can only delete the entire
tuple or nothing because as we know that we cannot update tuples."""

del variable_tuple

#print("\n\nWe Expect an error :",variable_tuple);

"""Note this first part is short down to the fact that tuple & list share alot of
the same functions which work very much the same with the exceptio  of 'tuple()' which
is used to convert lists type tuple."""

print("\n\n\nTEST-2\n-----------------------------\n");

#Variables - Dictionary.
variable_dictionary = {"Name":"Ryan Molyneux","Age":19,"Birthday": "11/02/1998","BirthCountry": "Ireland"};

print("\n\nExample of how to access elements of dictionary using 'keys'.\n");

print("\nName : ",variable_dictionary["Name"]);

print("\n\nAge : ",variable_dictionary["Age"]);

print("\n\nDate of Birth : ",variable_dictionary["Birthday"]);

print("\n\nCountry of birth : ",variable_dictionary["BirthCountry"]);

"""Notice that instead of using index's with the square brackets we are using 
string, which is optional aswell because we can use numbers also but its good
option."""

print("\n\nTEST-3\n-----------------------------------\n"); 


"""Now we are going to test updating&adding to dictionary which are identical in
syntax also we are going to test '.clear()' operation which removes all elements
from dictionary which deleting it & also the 'del' method that we have previously
covered."""

print("\nDictionary prior to update : ",variable_dictionary);

#Updating & Adding elements
variable_dictionary["Name"] = "Molyneux Ryan";
variable_dictionary["BirthCounty"] = "Dublin";

print("\n\nThis dictionary has been updated : ",variable_dictionary);

print("\nThis is the dictionary prior to clear : ",variable_dictionary);

#Clearing Dictionary.
variable_dictionary.clear();

print("\n\nAs you can see now the dictionary is empty : ",variable_dictionary);

#Note we will not clear the 'del' as it is consistent across deleteing all 
#variables.


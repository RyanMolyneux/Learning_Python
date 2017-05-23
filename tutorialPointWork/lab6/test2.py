#Python cntd... wth dictionary.

"""Just to recap the dictionary shares many similarities with lists in python, what differs is how you
access data, data is stored with a key which can be numbers or string values which are then used to 
access that data which can range from strings,numbers etc... unlike tupples data in dictionary is 
updatedable and it uses an extra feature to clear the dictionary of all its data '.clear()' which
can come in handy when you want to clear it without deleting everthing."""

print("\nTEST-1\n------------------------\n");

"""Some extra functions that we are going to cover on the dictionary is '.copy()' which is ecentially a shallow copy
of the dictionarys values, also '.fromkeys()' which has two different configurations you can pass in just the keys to
convert or the keys and a default value for all or for instance two lists which you wish to convert into dictionary
made up of keys and values but they must be of same length, One more thing is a check so that you are able to check
if the dictionary has a certain key before trying to access it."""

#Variables
	#Dictionarys
variable_dictionary = {"fName":"Ryan","Age": 19,"Country":"Ireland"};
variable_dictionary2 = {};
	#Lists
variable_list = ["lName","DOB","County"];
variable_list2 = ["Molyneux","11/02/1998","Dublin"];

#Copying of dictionary handy function quick & easy
print("\n\nDictionary : ",variable_dictionary);

variable_dictionary2 = variable_dictionary.copy();

print("\n\nCopy : ",variable_dictionary2);

#Converting lists to fill dictionary with keys & data
#None expected result.
variable_dictionary2 = variable_dictionary2.fromkeys(variable_list,variable_list2);

print("\n\nDictionary made from two seperate lists : ",variable_dictionary2);

#'has_key' deprecated.
"""
if(variable_dictionary.has_key("Dublin")==True):
	print("\n\nThis key does exist within this dictionary.");
else:
	print("\n\nSorry but this key does not exist within this dictionary.");

"""
#Aternative
if("Dublin" in variable_dictionary.keys()):
	print("\n\nThis key exists within this dictionary");
else:
	print("\n\nThis key does not exist within dictinary");

"""Okay that was a nice warm up not the part were we found deprecated function 
but still it was nice to know why some of the methods we have been using have
been saying that they are not defined."""

print("\n\nTEST-2\n----------------------------------\n");

"""Note one way of geting the current date time in Python is by using an abstract
class/module 'time' which you must import,this represented will second interval
ticks like so."""

#Imports
import time; #Import is Required

#Variables
variable_tick = time.time();

print("\n\nHow this time module displays : ",variable_tick);

"""Yes this can be very useful for dates and time but not those that come before
'1970' & After '2038',so how do we fix this?"""






























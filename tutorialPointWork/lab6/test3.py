#Python Revision on calendar

#Imports
import calendar;
import time;

#Variables
variable_time_tuple = time.localtime(time.time()); 


print("\n\nTEST-1\n---------------------------\n");

"""So again were just gonna quickly skimm over ticks,timeTuples & formating."""

print("\n\nSo first is ticks we acquired these by using 'time' modules method '.time()' like some : ",time.time());

print("""\n\nNote this is a representation of time passed since '12am 1 January 1970 Epoch' in a floating point value of
seconds.""");

print("""\n\nNow time for time '.localtime()' which passes in '.time()' as a parameter which is then converted into your
local time like so : \t """,variable_time_tuple[0],"<-Year \t",variable_time_tuple[1],"<- Month \t\t",variable_time_tuple[2],"<- Day.");

print("""\n\nNext is time '.asctime' method which is part of the 'time' module which can be used to neatly represent the current
time like so \n\n\nCurrent Time Formated : """,time.asctime(variable_time_tuple));

print("\n\n\tTEST-2\n---------------------------\n");


"""So that was the 'time' module or class now what we want to go back over is the 'calendar' module/class using
the first method '.month()' which is used to show a neat representation of the current day's in a month of a 
certain year."""

print("\n\nDays of the month in Febuary 2018 using '.month(2018,22)' \n-----------------------------\n\n",calendar.month(2018,2));


print("\n\nNow that we have made a nice calender we are going to check if 2018 is a leap year like so.\n");

#Notice that we never create or edit the instance of 'time','calendar' that is because these are abstract.

if(calendar.isleap(2018)==True):
	print("\n\nThis is a leap Year.");
else:
	print("\n\nThis is not  a leap Year.");

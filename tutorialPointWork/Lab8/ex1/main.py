#Imports
import menus;
from exceptions import *;

#Variables
#error = "This is my exception that extends runtime error class.";
#Functions

menus.title1();

menus.contentDesc("""\n\nThis section helps to demonstrate how you can create & use your own exception class\n below
one of those exceptions is printed. \n\n""");

try:
	raise ErrorError("errrrrror");
except ErrorError:
	print(ErrorError("EXCEPTION : Error Error exception has occured"));


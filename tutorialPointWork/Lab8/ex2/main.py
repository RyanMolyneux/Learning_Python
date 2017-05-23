#Imports
import extension;
import menus;

#Variables
school = extension.School();
firstName = "";
lastName = "";
parents = {"Father": "","Mother" : ""};
classes = ["Maths","English","Irish","Classical Studies","French","Art","History"];
age = 0;

#mainBody

menus.title1();
description = "\n\nWelcome to ",getattr(school,"name"),"\n\n";
menus.contentDesc(description);
firstName = input("\nPlease Enter First Name : ");
lastName = input("\n\nPlease Enter Last Name : ");
age = input("\n\nPlease Enter Your Age : ");
parents["Father"] = input("\n\nPlease Enter Your Fathers name : ");
parents["Mother"] = input("\n\nPlease Enter Your mothers name : ");

student = extension.Student(firstName,lastName,age,parents,classes); 

print("Congragulations You are now enrolled at ",getattr(school,"name"),"\nHere are the following details you submitted\n\n");
print("\nYour name : ",getattr(student,"firstName")+getattr(student,"lastName"));
print("\n\nYour age : ",getattr(student,"age"));
print("\n\nYour parents : ",getattr(student,"parents"));
print("\n\nClasses you will be attending are : ",getattr(student,"classes"));






menus.title2();

menus.contentDesc("\n\n\n\nWe would like to now test other functions such as 'issubclass' & 'isistance' which could come in handy\n\n");

input("\n\nWe are now going to check if our student checkin system works press enter to continue....");

if(getattr(student,"name") == getattr(school,"name") and isinstance(student,extension.Student) == True):
	print("\n\nCheck was Successfull you are a member of this school");
else:
	print("\n\nYou are not a student in this school.");


menus.title3();

menus.contentDesc("""\n\nI will now test data protection using double underscore
to then access this variable i must use the name of the class that created it like so.""");

print("\n(Using hiddent var Name)\n-------------\nNumber of students in the school",student._School__stuCount);

#As you might notice this causes a exception to be thrown because this variable is protected.
#print("\n\n(Calling variable)\n-------------\nNumber of students in the school",student.stuCount);









































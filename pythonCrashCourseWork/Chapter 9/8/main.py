#Chapter 9 ex 8 date 02/07/17.

#Imports
from users import Admin

#Variables

#Objects
site_admin = Admin("Robert","Malone","23","rm@gmail.com","ramus","password",{"Delete Users" : True,"Delete Posts" : False,"Edit Content" : True,"Add Content" : True})


#Functions

#Body

site_admin.check_priveledges()
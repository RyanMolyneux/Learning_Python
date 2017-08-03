#Chapter 9 ex 5 date : 28/06/17.

#Imports
from users import User

#Variables

#Objects
my_account = User("Ryan","M","1000","Miruzu","rm@gmail.com","rm1017")
#Functions

#Body

for index in range(0,7):
	my_account.increment_attempts()

print("\n\nNumber of attempts : ",my_account.login_attempts)

my_account.reset_attempts()

print("\n\nNumber of attempts : ",my_account.login_attempts)
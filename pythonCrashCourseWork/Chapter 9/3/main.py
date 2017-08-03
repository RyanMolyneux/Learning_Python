#Chapter 9 ex 3 date : 26/06/17.

#Imports
from users import User

#Variables

#Objects
my_account = User("Ryan","M","1000","Miruzu","rm@gmail.com","rm1017")
your_account = User("Samwell","Tarley","2000","Mizocko","sm@hotmail.com","sm17")
#Functions

#Body

my_account.describe_user()
your_account.describe_user()

my_account.greet_user(your_account)
your_account.greet_user(my_account)
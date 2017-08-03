"""This is the starting point for our app where all other python modules will be executed from."""
#Chapter 10 ex 8&9 DATE : 17/07/18.

#Imports
from functions import display_animals

#Variables
animal_list = []

#Objects - EMPTY

#Functions - EMPTY

#Body

print("\n\n--------------------------------\nKennels Animal \n--------------------------------\n\n"
      +"This program will prompt you for the names of files to find the names of the animals in\n"
      +"if you run into any problems please check that you included files extension when entering\n"
      +"the name.")

animal_list.append(input("\n\nDog file\nInput : "))

animal_list.append(input("\n\nCat file\nInput : "))


display_animals(animal_list)
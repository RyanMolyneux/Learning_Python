#Chapter 11 ex 3 DATE : 25/07/17.

#Imports - EMPTY
#Variables - EMPTY
#Objects - EMPTY 

#Classes
class Employee():
	"""Employee class used to demonstrate use of class test cases."""
	
	#Constructor
	def __init__(self,f_name,l_name,salary):
		self.f_name = f_name
		self.l_name = l_name
		self.salary = salary

	#Methods
	def award_raise(self,raiseAmount=5000):
		"""Method which adds raise to employee's monthly salary."""
		self.salary+= raiseAmount


#Functions - EMPTY
#Body - EMPTY
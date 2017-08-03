#Imports
import unittest
from main import Employee
#Classes

class EmployeeUnitTest(unittest.TestCase):
	"""Used to test the employee class in the module main.py"""
	
	#Unit Test Constructor
	def setUp(self):
		"""Used to try reduce redundancy in each test method."""
		self.testEmployee = Employee("Ryan","M",20000)
		
	
	def test_default_raise(self):
		"""Used to test that the classes default raise value is correct."""
		self.testEmployee.award_raise()
		self.assertEquals(self.testEmployee.salary,25000)
		
	def test_alt_raise(self):
		"""Used to test that method raise executes properly when not using default raise value."""
		self.testEmployee.award_raise(7500)
		self.assertEquals(self.testEmployee.salary,27500)
	
unittest.main()

#Imports
import city_functions
import unittest

class TestFormatFunctions(unittest.TestCase):
	"""Class that is generally used for testing functions that return formatted string values."""
	
	#Methods
	def test_destination_format_info(self):
		"""Method used to test a single function in city_functions module."""
		formatted_string = city_functions.format_destination_info("dublin","ireland")
		self.assertEqual(formatted_string,"Dublin, Ireland")
	
	def test_destination_format_info_optional(self):
		"""Method used to test if optional value if being properly formatted or used in string."""
		formatted_string = city_functions.format_destination_info("dublin","ireland","500000")
		self.assertEqual(formatted_string,"Dublin, Ireland - Population : 500000")
unittest.main()
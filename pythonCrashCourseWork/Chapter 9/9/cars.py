#Classes 

class Car():
	"""Class storing information about various cars."""
	
	#Constructor
	def __init__(self,manufacturer,model,year):
		"""Constructor to create & initialise variables for car class."""
		self.manufacturer = manufacturer
		self.model = model
		self.year = year

class ElectricCar(Car):
	"""A more specific version of car class that only models after electric cars."""
	

	#Constructor
	def __init__(self,manufacturer,model,year,battery):
		super().__init__(manufacturer,model,year)
		self.battery = battery


class Battery():

	#Constructor
	def __init__(self,battery_size=70,range=240):
		self.battery_size = battery_size
		self.range = range

	#Methods 
	
	def get_range(self):
		"""Method to check wether or not range needs updating & to print current travel range."""
		print("\n------------------------\nTravel Distance Capable\n------------------------\n")

		if self.battery_size == 85:
			self.range = 270

		print("\nYour Vehicle currently can travel ",str(self.range)," miles on a single charge.")


		

	def upgrade_battery(self):
		"""Used to perform upgrade on your electric cars battery."""

		print("\n-----------------------\nBattery Upgrade\n-----------------------\n")
		if self.battery_size < 85:
			self.battery_size = 85
			print("\nYour battery has been upgraded to ",str(self.battery_size)," kWh.")
		else:
			print("\n Your battery is already upgraded to ",str(self.battery_size)," kWh.") 
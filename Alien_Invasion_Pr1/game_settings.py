#Classes

class Settings():
	"""This class is used to setup & store the users current settings for the game."""
	
	#Constructor
	def __init__(self):

		#Bullet values
		self.bullet_speed = 1
		self.bullet_height = 10 
		self.bullet_width = 3
		self.bullet_cap = 5
		self.bullet_colour = (204,0,153)

		#Screen values
		self.screen_width = 1020
		self.screen_height = 640 
		self.bg_colour = (120,120,120)
		
		#Invader values
		self.invader_width = 75
		self.invader_height = 45
		self.invader_row_space = self.screen_width - (self.invader_width * 2)
		self.invader_row_cap = int(self.invader_row_space / (self.invader_width * 2))

		"""This will more easily allow us to adjust the current speed of the ship 
		by doing it in only one place."""
		self.ship_speed = 1.25
#Imports
import pygame

#Classes

class Ship():
	"""This class contains vaues & actions our ship can perform in Zims invasion."""
	
	#Constructor
	def __init__(self,screen,current_settings):
		
		#Creating attributes for passed in values in use.		
		self.screen = screen
		self.current_settings = current_settings
		

		#Load up ship image 
		self.image = pygame.image.load('images/starfighter.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#This sets up the start position on the display.
		self.rect.centerx = self.screen_rect.centerx
		
		#Creates float type of the ships current center for finer adjustment
		self.center = float(self.rect.centerx)

		self.rect.bottom = self.screen_rect.bottom

		#Movement flags
		self.move_right = False
		self.move_left = False

	#Methods
	
	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update_position(self):
		"""This method is used to check & perform the current movements of the ship."""
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.center += self.current_settings.ship_speed
		if self.move_left and self.rect.left > 0:
			self.center -= self.current_settings.ship_speed
			
		#Convert back to integer implicitly to perform movement
		self.rect.centerx = self.center	
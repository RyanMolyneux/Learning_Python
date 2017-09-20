#Imports
import pygame
from pygame.sprite import Sprite

#Classes
class Invader(Sprite):
	"""This will be the class used by the fleet of invaders."""

	#Constructor
	def __init__(self,current_settings,screen):
		
		#First call to super class as the invader is a type of sprite
		super(Invader,self).__init__()
		
		#Initialise those passed in as locals for later use
		self.current_settings = current_settings
		self.screen = screen

		#Load sprite image & rectangle of image area
		self.image = pygame.image.load("images/zimian_ship.bmp")
		self.rect = self.image.get_rect()
		
		#Set start position
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Now create float of x for finer adjustment of speed
		self.x_position = float(self.rect.x)
		
		
	#Methods

	def blitme(self):
		"""Used to display sprite on screen"""
		self.screen.blit(self.image,self.rect)
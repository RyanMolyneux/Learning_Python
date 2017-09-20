#Imports
import pygame
from pygame.sprite import Sprite

#Classes

class Bullet(Sprite):
	"""This is the ships bullet object which is a child class of sprite as it has no image."""
	
	#Constructor
	def __init__(self,current_settings,screen,ship):
		
		#Call to initialise super class otherwise known as parent.
		super(Bullet,self).__init__()
		
		self.screen = screen
		
		#Setting up bullets position
		self.my_rect = pygame.Rect(-1,0,current_settings.bullet_width,current_settings.bullet_height)
		self.my_rect.centerx = ship.rect.centerx
		self.my_rect.top = ship.rect.top 		

		#setup y position as float for finer readjustment
		self.y_position = float(self.my_rect.y)

		self.colour = current_settings.bullet_colour
		self.speed = current_settings.bullet_speed

	def draw_bullet(self):
		"""Used to draw the sprite on screen."""
		pygame.draw.rect(self.screen,self.colour,self.my_rect)
	
	def update(self):		
		"""Used to update the position of the bullet each time called."""
		#This decreases y value which confused me but then I realised 0 is the top of the screen.
		self.y_position -= self.speed
		
		#This then converts our float y to int & set our rects why to this y.
		self.my_rect.y = self.y_position
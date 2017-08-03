#Chapter 12 ex 2 DATE : 02/08/17.

#Imports
import sys
import pygame

#Variables
ground_colour = (0,230,0)
bg_colour = (0,0,200)

#Objects
"""This creates & open's a displays a panel of provide resolution."""
screen = pygame.display.set_mode((1080,640))

#Class
class Hero():
	"""Class for your character in the game."""
	
	#Constructor
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load("hero.bmp")
		self.rect  = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	
	#Methods
	def blitme(self):	
		"""Draw Character onto screen."""
		self.screen.blit(self.image,self.rect)
		
#Function

#Body

pygame.display.set_caption("A Hero's Adventure")
screen.fill(ground_colour)
hero = Hero(screen) 

while True:
	
	screen.fill(bg_colour)	
	hero.blitme()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	pygame.display.flip()

#Chapter 12 ex 1 DATE : 01/08/17.

#Imports
import sys
import pygame

#Variables
bg_colour = (0,0,150)

#Objects
pygame.init()
screen = pygame.display.set_mode((1080,640))
#Classes
#Functions

#Body

pygame.display.set_caption("Blue Sky's")
screen.fill(bg_colour)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#Note just realised this reloads the games screen row by row not all at once.
	pygame.display.flip()



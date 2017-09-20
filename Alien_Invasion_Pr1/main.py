# Project: 1, Name : Alien Invasion, DATE : 01/08/17.

#Imports
import pygame
import game_functions
from pygame.sprite import Group
from game_settings import Settings
from player_ship import Ship


#Variables -EMPTY

#Objects

"""Im assuming pygame object is always around from the looks of this this is 
simply preparing it for changes."""
pygame.init()

current_settings = Settings() 


#Screen Size set
screen = pygame.display.set_mode((current_settings.screen_width,current_settings.screen_height))

players_ship = Ship(screen,current_settings)
bullets = Group()


#Functions

def run_game():

	#This sets the screens caption		
	pygame.display.set_caption("Zim's Invasion.")

	#Create Empty invader group before main loop
	zimians = Group()

	#Then fill it up
	game_functions.create_fleet(current_settings,screen,zimians)
	
	while True:
		#Checks the type of event for exit from infinite loop
		
		
		game_functions.check_events(players_ship,screen,current_settings,bullets)
		players_ship.update_position()
		game_functions.update_bullets(bullets)
		
		game_functions.update_display(current_settings,screen,players_ship,zimians,bullets)

	

#Body
run_game() 
#Imports
import sys 
import pygame
from invader_ship import Invader
from bullet import Bullet
#Functions

def check_events(players_ship,screen,current_settings,bullets):
	"""This function is used to check the current events being performed in this game."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#Peforms the check for key's pressed & set's flags to true.
		if event.type == pygame.KEYDOWN:
			check_key_down(event,screen,current_settings,bullets,players_ship)

		#Performs a check for keys that have been relesed & sets thee flags to false.
		if event.type == pygame.KEYUP:
			check_key_up(event,players_ship)
#Check Key Function
def check_key_down(event,screen,current_settings,bullets,ship):
	"""Used to check what key was pressed down & act accordingly"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	elif event.key == pygame.K_SPACE and len(bullets) < current_settings.bullet_cap:
		fire_bullet(current_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
			

def check_key_up(event,ship):
	"""Used to check what key you lifted your finger from & act accordingly"""
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False			

def update_display(current_settings,screen,players_ship,zimians,bullets):
	"""Used to update & display current events happening on te display."""
	
	#Sets the games background colour.
	screen.fill(current_settings.bg_colour)
	
	#Used to redraw the players ship in its current position back to the screen
	players_ship.blitme()
	
	#Draws the zimian ship to display
	for zimian in zimians.sprites():
		zimian.blitme()

	for bullet in bullets.sprites():
		bullet.draw_bullet()


	#Updates the screen to next frame for smooth motion
	pygame.display.flip()

def update_bullets(bullets):
	"""Used to update the position of the bullets & ensure they are deleted when they go of screen."""
	bullets.update()
		
	#Used to remove bullets that go of display Note you must use the copy method when deleting.
	for bullet in bullets.copy():
		if bullet.my_rect.bottom <= 0:
			bullets.remove(bullet) 

def fire_bullet(current_settings,screen,ship,bullets):
	"""Used to reduce clutter of code in the program."""
	bullet = Bullet(current_settings,screen,ship)
	bullets.add(bullet)	

def create_fleet(current_settings,screen,zimians):
	"""Function used to form invader fleet on screen."""

	for current_row_fill in range(current_settings.invader_row_cap):
				
		zimian = Invader(current_settings,screen)
		zimian.x_position = current_settings.invader_width + (current_settings.invader_width * 2)*current_row_fill 
		zimian.rect.x = zimian.x_position
		zimians.add(zimian)
		
	


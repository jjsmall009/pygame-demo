"""
Programmer:		JJ Small
Class:			CSCI 321 - Game Programming
Project:		Game 01 - 2D Pygame
Description:	This is the main module for this game.  It Handles
				the game loop and all of that jazz.
"""

import pygame, random, sys, time
import main_menu, player, Platforms, fireball
from pygame.locals import *

# Initialize some variables
width = 1600
height = 900

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Escape From the Pit")
pygame.init()

# Play the game
def game_loop(screen):
	# FPS and game initialization
	FPS = 30
	game_clock = pygame.time.Clock()
	game_bg = pygame.image.load('../images/background.png')
	fb_effect = pygame.mixer.Sound('../audio/fireball-audio3.wav')
	WHITE = (255,255,255)

	screen.blit(game_bg,(0,0))
	pygame.display.update()

	# Sprite group to hold platformsq
	platform_list = pygame.sprite.Group()
	player_list = pygame.sprite.Group()
	fireball_list = pygame.sprite.Group()
	all_sprites = pygame.sprite.Group()

	# Create platforms at random locations on the screen
	for i in range(20):
		platform = Platforms.Platforms()
		platform.rect.x = random.randrange(140,1365)
		platform.rect.y = random.randrange(0,600)

		# Check to see if a new platform overlaps any other platform
		plat_collision = pygame.sprite.spritecollide(platform,platform_list,False)
		# If there is an overlap, change the position of the new platform
		for plat in plat_collision:
			if platform.rect.x < 1300:
				platform.rect.x -= 100
			if platform.rect.x < 139:
				platform.rect.x += 100
				platform.rect.y += 40

		# Check for platoform collisions
		while len(plat_collision) > 0:
			platform.rect.y -= 200
			platform.rect.x += 100
			plat_collision = pygame.sprite.spritecollide(platform,platform_list,False)

		platform_list.add(platform)
		all_sprites.add(platform)

	# Create the player object
	player1 = player.Player()
	player_list.add(player1)
	all_sprites.add(player1)

	# Create the fireballs
	fb1 = fireball.Fireball(400,755)
	fireball_list.add(fb1)
	all_sprites.add(fb1)

	frame_counter = 0
	seconds = 0
	font = pygame.font.Font(None, 35)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pause_menu(screen)

		# Do the timer stuff
		if frame_counter % 30 == 0:
			time_string = "Time alive: %s" % seconds
			text = font.render(time_string, True, WHITE)
			screen.blit(game_bg,(0,0))
			screen.blit(text, (735, 865))
			seconds += 1

		# Create fireballs at random intervals
		fireball_chance = random.randrange(0,10000)
		if fireball_chance < 200:
			fb_x = random.randrange(140,1265)
			fball = fireball.Fireball(fb_x,755)

			fireball_list.add(fball)
			all_sprites.add(fball)

			fb_effect.play()

		# Update the sprite groups and then draw everything to the screen
		all_sprites.clear(screen, game_bg)
		platform_list.update(platform_list)

		# Do some collision
		player1.rect.inflate(-5,-15)
		collision_list = pygame.sprite.spritecollide(player1,platform_list,False)
		player_list.update(collision_list, fireball_list)
		fireball_list.update()

		all_sprites.draw(screen)
		# If the player sprite is removed from the list, it means the player has
		# died and will trigger the game_over()
		if len(player_list) == 0:
			game_over(screen)

		# FPS stuff
		frame_counter += 1
		game_clock.tick(FPS)
		pygame.display.update()

# game over function.  brings up the game over menu
def game_over(screen):
	game_over_bg = pygame.image.load('../images/game-over.png')
	screen.blit(game_over_bg,(592,311))
	pygame.display.update()

	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				done = True
			if event.type == KEYDOWN:
				if event.key == K_y:
					game_loop(screen)
				elif event.key == K_q:
					done = True
					sys.exit(0)

		time.sleep(.25)

# Pause menu function.
def pause_menu(screen):
	pause_bg = pygame.image.load('../images/menu-pause.png')
	screen.blit(pause_bg,(0,0))
	pygame.display.update()

	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					done = True

		time.sleep(.25)



# Main function.  Handles all of the stuff
def main():

	# Try and load the game music
	try:
		pygame.mixer.init()
		pygame.mixer.music.load('../audio/menu-audio.ogg')
		pygame.mixer.music.play(-1)
	except:
		raise UserWarning, "could not load background music"


	# Create an instance of the main menu and then run its loop
	main = main_menu.main_menu()
	main.menu_loop(screen, width, height)

	# Once the main menu exits, that means the game has started
	game_loop(screen)

	pygame.quit()

# Create the main() thing
if __name__ == '__main__': main()

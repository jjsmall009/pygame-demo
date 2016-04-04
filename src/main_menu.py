"""
Programmer:		JJ Small
Description:	The main menu module.  A bust waiting loop that gets input
				and blits the menu images to the screen.
"""

import pygame, time, sys
from pygame.locals import *

menu_FPS = 10
menu_clock = pygame.time.Clock()

# Main menu class.  Handles all of the menu logic
class main_menu(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		# Give the menu the background menu image
		self.image = pygame.image.load('../images/main-menu.png')
		self.bg = pygame.image.load('../images/background.png')
		self.index = 0
		self.counter = 0
		self.images = []
		self.images.append(pygame.image.load('../images/lava2.png'))
		self.images.append(pygame.image.load('../images/lava3.png'))
		self.images.append(pygame.image.load('../images/lava4.png'))
		self.images.append(pygame.image.load('../images/lava5.png'))
		self.images.append(pygame.image.load('../images/lava6.png'))


		self.rect = self.image.get_rect()

	# Main menu loop.  Get input and process accordingly.
	def menu_loop(self, screen, width, height):

		# Load all of the menu images
		menu_dmd = pygame.image.load('../images/menu-dmd.png')
		menu_help_bg = pygame.image.load('../images/menu-help.png')
		menu_controls_bg = pygame.image.load('../images/menu-controls.png')
		menu_about_bg = pygame.image.load('../images/menu-about.png')

		# A bunch of booleans to indicicate where the mouse is at
		mouse_on_start = False
		mouse_on_help = False
		mouse_on_controls = False
		mouse_on_about = False
		mouse_on_quit = False
		mouse_on_back = False

		# Loop through
		done = False
		while not done:
			screen.blit(self.bg,(0,0))
			screen.blit(self.image, (0,0))

			# Loop through events
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				# Start the game
				if event.type == MOUSEBUTTONDOWN and mouse_on_start == True:
					done = True
				# Go to help submenu
				elif event.type == MOUSEBUTTONDOWN and mouse_on_help == True:
					self.sub_menu(self, screen, menu_help_bg)
				# Go to controls submenu
				elif event.type == MOUSEBUTTONDOWN and mouse_on_controls == True:
					self.sub_menu(self, screen, menu_controls_bg)
				# Go to about submenu
				elif event.type == MOUSEBUTTONDOWN and mouse_on_about == True:
					self.sub_menu(self, screen, menu_about_bg)
				# Break the loop and quit the game
				elif event.type == MOUSEBUTTONDOWN and mouse_on_quit == True:
					sys.exit(0)


			# Reset the mouse location booleans
			mouse_on_quit = mouse_on_start = mouse_on_about =  \
							mouse_on_help = mouse_on_controls = False

			# See where the mouse is at and change the mouse booleans
			mouse = pygame.mouse.get_pos()
			if 866 > mouse[0] > 673 and 287 > mouse[1] > 259:
				screen.blit(menu_dmd, (618,255))
				mouse_on_start = True
			elif  738 > mouse[0] > 673 and 354 > mouse[1] > 324:
				screen.blit(menu_dmd, (617,324))
				mouse_on_help = True
			elif  807 > mouse[0] > 673 and 420 > mouse[1] > 393:
				screen.blit(menu_dmd, (615,391))
				mouse_on_controls = True
			elif 862 > mouse[0] > 673 and 489 > mouse[1] > 463:
				screen.blit(menu_dmd, (613,458))
				mouse_on_about = True
			elif 730 > mouse[0] > 673 and 560 > mouse[1] > 530:
				screen.blit(menu_dmd, (611,525))
				mouse_on_quit = True

			# Do lava stuff
			if self.counter % 1 == 0:
				self.index += 1
				if self.index >= 5:
					self.index = 0
				screen.blit(self.images[self.index], (0,678))
			# Update the screen and tick the menu clock
			self.counter += 1
			pygame.display.update()
			menu_clock.tick(menu_FPS)

	# Load the help submenu and process events and such
	@staticmethod
	def sub_menu(self, screen, background):
		back_arrow_glow = pygame.image.load('../images/back-arrow-glow.png')
		mouse_on_back = False
		screen.blit(self.bg,(0,0))

		done = False
		while not done:
			screen.blit(background,(0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				if event.type == MOUSEBUTTONDOWN and mouse_on_back == True:
					done = True

			mouse = pygame.mouse.get_pos()
			# Check the mouse position for the back arrow
			if 1023 > mouse[0] > 982 and 581 > mouse[1] > 555:
				screen.blit(back_arrow_glow,(982,552))
				mouse_on_back = True

			# Do lava stuffb
			if self.counter % 1 == 0:
				self.index += 1
				if self.index >= 5:
					self.index = 0
				screen.blit(self.images[self.index], (0,678))

			pygame.display.update()
			menu_clock.tick(menu_FPS)

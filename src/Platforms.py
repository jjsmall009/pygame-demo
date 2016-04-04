"""
Programmer:		JJ Small
Class:			CSCI 321 - Game Programming
Project:		Game 01 - 2D Pygame
Description:	Platform module.  Does platform stuff
"""

import pygame, sys, random
from pygame.locals import *

class Platforms(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		# Platform attributes
		self.image = pygame.image.load('../images/platform2.png')
		self.rect = self.image.get_rect()

	# When a platform reaches the lava pit, this function is called and resets
	# its position to the top of the screen.
	def reset_pos(self, plat_list):
		self.rect.x = random.randrange(140,1365)
		self.rect.y = random.randrange(0,300)

		# Check to see if a new platform overlaps any other platform
		plat_col = pygame.sprite.spritecollide(self,plat_list,False)
		# If there is an overlap, change the position of the new platform
		while len(plat_col) > 1:
			self.rect.y -= 200
			self.rect.x += 100
			plat_col = pygame.sprite.spritecollide(self,plat_list,False)
		
	# Simple update function that moves the platform down at a rate of 2 pixels per frame
	def update(self, plat_list):		
		height = 744
		#platform_glow = pygame.image.load('../images/platform-glow.png')
		self.rect.y += 2
		if self.rect.top > height:
			#screen.blit(platform_glow,(self.rect.x,self.rect.y))
			self.reset_pos(plat_list)

"""
Programmer:		JJ Small
Description:	Fireball module, creates it.
"""

import pygame, sys, random
from pygame.locals import *

class Fireball(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.images = []
		# Add the fireball images to our image list
		self.images.append(pygame.image.load('../images/fireballs/fb1.png'))
		self.images.append(pygame.image.load('../images/fireballs/fb2.png'))
		self.images.append(pygame.image.load('../images/fireballs/fb3.png'))

		self.index = 0 # keep track of which frame I'm in for the animation
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.frame_counter = 0

	# Moves the fireball on the screen.
	def update(self):
		self.frame_counter += 1
		# Get rid of the fireball when it moves off screen.
		if self.rect.y < -100:
			self.kill
		else:
			self.rect.y -= 8
			# This is how we animate the fireball.  Every 5 frames, changes the
			# images to the next one in the list
			if self.frame_counter % 5 == 0:
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]

"""
Programmer:		JJ Small
Class:			CSCI 321 - Game Programming
Project:		Game 01 - 2D Pygame
Description:	Player module.  Creates a player object and has a lot of
				functions to handle the player logic.
"""

import pygame, sys, random, time
import Platforms
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# Load the sprite images.  Gotta find a better way to do it
		self.images = []
		self.images.append(pygame.image.load('../images/player_sprites/left1.png'))
		self.images.append(pygame.image.load('../images/player_sprites/left2.png'))
		self.images.append(pygame.image.load('../images/player_sprites/left3.png'))
		self.images.append(pygame.image.load('../images/player_sprites/left4.png'))
		self.images.append(pygame.image.load('../images/player_sprites/right1.png'))
		self.images.append(pygame.image.load('../images/player_sprites/right2.png'))
		self.images.append(pygame.image.load('../images/player_sprites/right3.png'))
		self.images.append(pygame.image.load('../images/player_sprites/right4.png'))
		self.images.append(pygame.image.load('../images/player_sprites/facing.png'))

		# Initialize a lot more things
		self.image = self.images[8]
		self.rect = self.image.get_rect()
		self.left_index = self.right_index = self.frame_counter = 0
		self.rect.y = self.x_change = self.y_change = self.yVelocity = 0
		self.speed = 8
		self.gravity = 1.0
		self.rect.x = 800
		self.falling = True
		self.standing = self.jumping = False
		self.current_platform = Platforms.Platforms()

	# Jump function, pretty simple
	def jump(self):
		self.jumping = True
		self.falling = False
		self.standing = False
		self.yVelocity = -16

	def move_left(self):
		if self.rect.left < 120:
			self.x_change = 0
		else:
			self.x_change = -self.speed
		# Change the anaimation frame
		if self.frame_counter % 5 == 0:
			self.left_index += 1
			if self.left_index >= 4:
				self.left_index = 0
			self.image = self.images[self.left_index]

	def move_right(self):
		if self.rect.right > 1475:
			self.x_change = 0
		else:
			self.x_change = self.speed
		# change the animation frame
		if self.frame_counter % 5 == 0:
			self.right_index += 1
			if self.right_index >= 4:
				self.right_index = 0
			self.image = self.images[self.right_index+4]

	# This big function handles updating the player, such as movement 
	# and collisions and such
	def update(self, collision_list, fireball_list):
		self.frame_counter += 1
		self.x_change = self.y_change = 0
		# Ket the keyboard input
		user_input = pygame.key.get_pressed()
		if user_input[K_UP] and self.standing:
			self.jump()
		elif user_input[K_LEFT]:
			self.move_left()
		elif user_input[K_RIGHT]:
			self.move_right()

		# The default state of the player is falling.
		if self.falling:
			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity
			# self.y_change += self.speed
			# self.rect.y += self.y_change
			if self.rect.bottom > 775:
				self.kill()

		# Update the players horizontal movement
		self.rect.x += self.x_change
		
		# Go some gravity stuff when you jump
		if self.jumping:
			self.yVelocity += self.gravity
			self.rect.y += self.yVelocity
			if self.yVelocity > 0:
				self.yVelocity = 0
				self.jumping = False
				self.falling = True
			
		# Check for collisions with a platform, and the stand on it.
		if not self.jumping:
			for plat in collision_list:
				if self.rect.bottom-50 < plat.rect.top < self.rect.bottom+50:
					self.current_platform = plat
					self.falling = False
					self.standing = True

		# Check if you got hit by a fireball
		fball_collision_list = pygame.sprite.spritecollide(self, fireball_list, True)
		if len(fball_collision_list) > 0:
			self.kill()
		
		# Check if you've fallen off of the platform
		if self.standing:
			self.rect.bottom = self.current_platform.rect.top+3
			new_rect = self.rect.inflate(-10,0)
			# If you've moved off of the edge, fall off the platform
			if new_rect.bottomright < self.current_platform.rect.topleft \
					or new_rect.bottomleft > self.current_platform.rect.topright:
				self.yVelocity = 0
				self.current_platform = None
				self.standing = False
				self.falling = True

		if self.rect.x < 0:
			self.rect.x = 0
			if self.rect.bottom > 744:
				self.current_platform = None
				self.falling = True
				self.standing = False
				self.yVelocity = 0

	
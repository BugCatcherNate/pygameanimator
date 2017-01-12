import pygame, sys, spritesheet, time, animator
from pygame.locals import *

pygame.init()
animator = animator.animator(50, 75, "Charactervector.png")

class mainMovement:

	

	def __init__(self, startx, starty, screenx, screeny, bgimage, displaysurf):
		
		self.imgx = startx
		self.imgy = starty
		self.screenx = screenx
		self.screeny = screeny
		self.bg = pygame.image.load(bgimage).convert()
		self.pressed_right = False
		self.pressed_down = False
		self.pressed_left = False 	
		self.pressed_up = False
		self.displaysurf = displaysurf
		self.change = False
		self.animator = animator
		self.img = self.animator.stationary()

	def position(self):

		if self.pressed_right:

			if self.imgx != 1000:
			
	
				self.imgx += 5
				self.img = animator.animation(3, 4)
			
		elif self.pressed_down:
				
			if self.imgy != 1000:
			
			
				self.imgy += 5
				self.img = animator.animation(0, 4)
			
		elif self.pressed_left:
				
			if self.imgx != 10:
			
		
				self.imgx -= 5
				self.img = animator.animation(2, 4)
						
		elif self.pressed_up:
				
			if self.imgy != 10:
	
		
				self.imgy -= 5
				self.img = animator.animation(1, 4)	


		

		if self.change == True:			
			self.displaysurf.blit(self.bg, (0, 0), (self.imgx, self.imgy, self.screenx, self.screeny))
			self.displaysurf.blit(self.img.convert(), (self.screenx/2, self.screeny/2))	

			pygame.display.update()



	def movement(self, event):

		if event.type == KEYDOWN:
				
				self.change = True
				if event.key == K_d:
					self.pressed_right = True
				
				elif event.key == K_s:
					self.pressed_down = True
				
				elif event.key == K_a:
					self.pressed_left = True

				elif event.key == K_w:
					self.pressed_up = True
				
		elif event.type == KEYUP:
				self.change = False
				if event.key == K_d:
					self.pressed_right = False
				
				
				elif event.key == K_s:
					self.pressed_down = False
					self.img = animator.stationary()
				
				
				elif event.key == K_a:
					self.pressed_left = False
				
				elif event.key == K_w:
					self.pressed_up = False	


		


	def actions(self, events):

		
		for event in events:

			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			self.movement(event)
		self.position()

			
	

			
			

	




import pygame
import random

class Tail:
	def __init__(self, posx, posy, width, height):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.R = random.randint(0, 255) 
		self.G = random.randint(0, 255)
		self.B = random.randint(0, 255)
	def draw(self, Display):
		pygame.draw.rect(Display, [self.R, self.G, self.B], [self.posx, self.posy, 16, 16])

	def move(self, px, py):
		self.posx = px
		self.posy = py
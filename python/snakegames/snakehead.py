import pygame

class Snakehead:
	def __init__(self, posx, posy, width, height):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.movement = 'null'
		self.speed = 5
	def draw(self, Display):
		pygame.draw.rect(Display, [0, 0, 0], [self.posx, self.posy, self.width, self.height])
	def read_input(self, key):
		if key == pygame.K_a or key == pygame.K_LEFT:
			self.movement = 'left'
		elif key == pygame.K_d or key == pygame.K_RIGHT:
			self.movement = 'right'
		elif key == pygame.K_w or key == pygame.K_UP:
			self.movement = 'up'
		elif key == pygame.K_s or key == pygame.K_DOWN:
			self.movement = 'down'
		print(self.movement)
	def get_pos(self):
		return self.posx, self.posy

	def restart(self, ScreenW, ScreenH):
		self.posx = ScreenW / 2 - 16/2
		self.posy = ScreenH / 2 - 16/2
	def move(self, SW, SH):
		if self.posx < 0 or self.posx + 16 > SW:
			self.restart(1280, 720)
			#restart
		elif self.posy < 0 or self.posy + 16 > SH:
			self.restart(1280, 720)
			#restart

		if self.movement == 'right':
			self.posx += self.speed
		elif self.movement == 'left':
			self.posx -= self.speed
		elif self.movement == 'up':
			self.posy -= self.speed
		elif self.movement == 'down':
			self.posy += self.speed
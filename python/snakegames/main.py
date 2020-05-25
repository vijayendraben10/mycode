import pygame
import snakehead
import food
import tail
import random

ScreenW = 1280
ScreenH = 720

sheadX = 0
sheadY = 0

fX = 0
fY = 0

gameover = False

pygame.init()
pygame.display.set_caption("Snake Game")

Display = pygame.display.set_mode([ScreenW, ScreenH])
Display.fill([255, 255, 255]) #RGB white

shead = snakehead.Snakehead(ScreenW / 2 - 16/2, ScreenH / 2 - 16/2, 16, 16)
f = food.Food(random.randint(0, (ScreenH - 16)/16) * 16 + 8, random.randint(0, (ScreenW - 16)/16) * 16 + 8, 16, 16)
tails = []

Fps = 20
timer_clock = pygame.time.Clock()

while not gameover:
	Display.fill([255, 255, 255]) 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True
			break
		elif event.type == pygame.KEYDOWN:
			shead.read_input(event.key)
	shead.move(ScreenW, ScreenH)
	shead.draw(Display)
	f.draw(Display)
	sheadX, sheadY = shead.get_pos()
	fX, fY = f.get_pos()
	#detect collision
	if sheadX + 16 > fX and sheadX < fX + 16:
		if sheadY + 16 > fY and sheadY < fY + 16:
			#collision
			f.respawn(ScreenW, ScreenH)
			if tails == []:
				tails.append(tail.Tail(sheadX, sheadY, 16, 16, shead. get_movement))
	shead.move(ScreenW, ScreenH)
	shead.draw(Display)
	for tail in tails:
		tail.draw(Display)
	f.draw(Display)
	pygame.display.flip()
	pygame.display.update()
	timer_clock.tick(Fps) 

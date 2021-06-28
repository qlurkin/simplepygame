import pygame
from pygame import draw, event, font, image, key, mouse, Rect, Surface, time, display, Color, mixer, music, transform, math, version
from pygame.locals import *

def init(size):
	pygame.init()
	screen = pygame.display.set_mode(size)
	return screen

def loop(fun):
	clock = pygame.time.Clock()
	state = tuple()
	while True:
		clock.tick(30)
		if pygame.event.peek(pygame.QUIT):
			break
		screen = pygame.display.get_surface()
		pygame.draw.rect(screen, (0, 0, 0), screen.get_rect())
		state = fun(*state)
		pygame.display.flip()

def save(surface, filename):
	pygame.image.save(surface, filename)

def done():
	pygame.display.flip()
	while True:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			break

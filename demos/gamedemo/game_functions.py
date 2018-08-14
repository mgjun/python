import sys

import pygame

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_down_events(event,ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def check_down_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False


def  update_screen(sys_settings,screen,ship):
	screen.fill(sys_settings.bg_color)
	ship.blitme()
	pygame.display.flip()

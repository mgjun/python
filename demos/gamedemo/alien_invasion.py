import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	sys_settings = Settings()
	screen = pygame.display.set_mode((sys_settings.screen_width,sys_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (230,230,230)
	ship = Ship(sys_settings,screen)
	bullets = Group()

	while True:
		gf.check_events(sys_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(sys_settings,screen,ship,bullets)

run_game()

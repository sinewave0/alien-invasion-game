import sys 
import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
import game_functions as gf
def run_game():
    pygame.init()
    # test commment
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion Game Beta")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    bg_color = (230,230,230)

    while True:
        gf.check_events(ai_settings, screen,ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        #print(len(bullets)) 
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()

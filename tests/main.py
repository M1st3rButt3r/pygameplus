import sys

import pygame

sys.path.append('../src')

import pygameplus.game_object

pygameplus.init()
image = pygame.Surface((20, 20))
image.fill((255, 255, 255))
go = pygameplus.game_object.GameObject(sprite=image, position=(300, 300))
pygameplus.launch()

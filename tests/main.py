import sys

sys.path.append('../src')

import pygameplus.game_object
import pygame

pygameplus.init()

image = pygame.Surface((20, 20))
image.fill((255, 0, 255))
pygameplus.game_object.GameObject(image)

image2 = pygame.Surface((20, 20))
image2.fill((0, 0, 255))
pygameplus.game_object.GameObject(image2).set_layer(1)

pygameplus.launch()

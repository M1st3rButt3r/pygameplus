import pygame
import pygameplus


class GameObject(pygame.sprite.Sprite):
    def __init__(self, sprite=pygame.Surface((1, 1)), position=(0, 0)):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        pygameplus.game_objects.add(self)

    def update(self):
        return

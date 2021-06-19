import pygame
from . import rendering


class GameObject(pygame.sprite.Sprite):
    def __init__(self, sprite=pygame.Surface((1, 1)), position=(0, 0), layer=0):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.render_layer = None
        self.set_layer(layer)

    def update(self):
        return

    def set_layer(self, render_layer):
        if self.render_layer is not None:
            self.groups()[0].remove(self)

        if rendering.render_layers.keys().__contains__(render_layer):
            rendering.render_layers[render_layer].add(self)
            self.render_layer = render_layer
        else:
            rendering.add_render_layer(render_layer)
            rendering.render_layers[render_layer].add(self)
            self.render_layer = render_layer
        return self

import collections
import pygame

render_layers = collections.OrderedDict()


def add_render_layer(render_layer_id):
    global render_layers
    new_layer = pygame.sprite.Group()
    render_layers.update({render_layer_id: new_layer})
    render_layers = collections.OrderedDict(sorted(render_layers.items()))

import pygame
import sys
from . import rendering

# Options
caption = "Game"
screen_size = [600, 600]


def init():
    global clock
    pygame.init()
    clock = pygame.time.Clock()
    rendering.add_render_layer(0)


def setup():
    global screen
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(caption)


def update():
    for layer in rendering.render_layers.values():
        for game_object in layer:
            game_object.update()


def draw():
    screen.fill((0, 0, 0))
    for layer in rendering.render_layers.values():
        layer.draw(screen)
    pygame.display.update()


def game_loop():
    setup()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
        update()
        draw()
        clock.tick(60)


def launch():
    game_loop()

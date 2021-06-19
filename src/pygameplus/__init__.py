import pygame
import sys

# Options
caption = "Game"
screen_size = [600, 600]


def init():
    global clock
    global game_objects
    pygame.init()
    clock = pygame.time.Clock()
    game_objects = pygame.sprite.Group()


def setup():
    global screen
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(caption)


def update():
    for game_object in game_objects:
        game_object.update()


def draw():
    screen.fill((0, 0, 0))
    game_objects.draw(screen)
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

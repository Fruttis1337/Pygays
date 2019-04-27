import pygame
from pygame import *

WIN_WIDTH = 1400
WIN_HEIGHT = 900

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_capture = 'Game'
    bg_image = pygame.image.load('C:\\Users\\lib\\PyGays\\img\\background.jpg')
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
                break
        screen.blit(bg_image, (0, 0))
        pygame.display.flip()
        clock.tick(60)


main()

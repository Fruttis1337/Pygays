import pygame
from pygame import *
from GameWorld import World
from Coin import Coin
from Platform import Platform

WIN_WIDTH = 1400
WIN_HEIGHT = 900

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_capture = 'Game'
    bg_image = pygame.image.load('background.jpg')
    game = True
    #считать файл уровня
    world = World()  #дописать
    bx = 0  #доделать размер карты
    by = 0  #доделать размер карты

    while game:#глобальный цикл на проверку стейта вставить
        board = list(['' * bx] * by)
        for i in world.get_platforms():
            board[i.get_coords()[1]][i.get_coords()[0]] = i
        for i in world.get_coins():
            board[i.get_coords()[1]][i.get_coords()[0]] = i
        for i in world.get_enemies():
            board[i.get_coords()[1]][i.get_coords()[0]] = i
        for i in world.get_boss():
            board[i.get_coords()[1]][i.get_coords()[0]] = i
        for e in pygame.event.get():
            if e.type == QUIT:
                game = False
                break
            #взаимодействия с кнопками и игроком

            screen.blit(bg_image, (0, 0))
            #проход по world, изменеие картинки в board и отрисовка
            pygame.display.flip()
            clock.tick(60)


main()
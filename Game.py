import pygame
from pygame import *
from GameWorld import World
from Coin import Coin
from Platform import Platform
from Enemy import Enemy, Boss

WIN_WIDTH = 1400
WIN_HEIGHT = 900

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_capture = 'Game'
    bg_image = pygame.image.load('background.jpg')
    game = True
    level = open('level.txt')
    bx, by = list(map(int, level.readline().split()))
    plats = []
    cns = []
    enm = []
    bs = []
    state = 1 # 1 - меню, 2 - игра, 3 - смерть
    phr = level.readline().split()  # считываем уровень
    for i in range(0, len(phr), 3):
        plats.append(Platform(int(phr[i]), int(phr[i + 1]), bool(phr[i + 2])))
    phr = level.readline().split()
    for i in range(0, len(phr), 2):
        cns.append(Coin(int(phr[i]), int(phr[i + 1])))
    phr = level.readline().split()
    for i in range(0, len(phr), 2):
        enm.append(Enemy(int(phr[i]), int(phr[i + 1])))
    phr = level.readline().split()
    for i in range(0, len(phr), 2):
        bs.append((int(phr[i]), int(phr[i + 1])))
    world = World([(0, 0)], plats, cns, enm, bs)  # конец считывания уровня


    while game:  # TODO:глобальный цикл на проверку стейта вставить
        if state == 1:
            pass  # TODO:написать меню
        elif state == 2:
            screen.blit(bg_image, (0, 0))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
            for i in world.get_platforms():
                i(screen)
            for i in world.get_coins():
                i(screen)
            for i in world.get_enemies():
                i(screen)
            for i in world.get_boss():
                i(screen)

            #TODO:взаимодействия с кнопками и игроком
            #TODO:пройтись по world и поменять значения
        elif state == 3:
            pass  #TODO:написать меню смерти

    pygame.display.flip()
    clock.tick(60)


main()
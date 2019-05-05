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
    state = 1  # 1 - меню, 2 - игра, 3 - смерть, 4 - уровни, 5 - титры
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
            screen.fill(pygame.Color('Green'))
            f2 = pygame.font.SysFont('serif', 48)
            txt1 = f2.render('Играть', 1, (255, 255, 255))
            txt2 = f2.render('Уровни', 1, (255, 255, 255))
            txt3 = f2.render('Авторы', 1, (255, 255, 255))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 200, 600, 100))
            screen.blit(txt1, (625, 225, 600, 100))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 350, 600, 100))
            screen.blit(txt2, (625, 375, 600, 100))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 500, 600, 100))
            screen.blit(txt3, (625, 525, 600, 100))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        game = False
                        break
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if e.pos[0] in range(400, 1000):
                            if e.pos[1] in range(200, 300):
                                state = 2
                            elif e.pos[1] in range(350, 450):
                                state = 4
                            elif e.pos[1] in range(500, 600):
                                state = 5
                        pygame.draw.circle(screen, pygame.Color('Red'), e.pos, 20)
                        pygame.display.update()
            pygame.display.flip()
            clock.tick(60)

        elif state == 2:
            screen.blit(bg_image, (0, 0))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        state = 1
                        pass
                        # game = False TODO: реализовать паузу
                        # break
            for i in world.get_platforms():
                i(screen)
            for i in world.get_coins():
                i(screen)
            for i in world.get_enemies():
                i(screen)
            for i in world.get_boss():
                i(screen)
            pygame.display.flip()
            clock.tick(60)

            # TODO:взаимодействия с кнопками и игроком
            # TODO:пройтись по world и поменять значения
        elif state == 3:
            screen.fill(pygame.Color('Yellow'))
            f2 = pygame.font.SysFont('serif', 48)
            txt0 = f2.render('СМЕРТ', 1, pygame.Color('Red'))
            txt1 = f2.render('Заново', 1, (255, 255, 255))
            txt2 = f2.render('Меню', 1, (255, 255, 255))
            screen.blit(txt0, (625, 100, 600, 100))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 200, 600, 100))
            screen.blit(txt1, (625, 225, 600, 100))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 350, 600, 100))
            screen.blit(txt2, (625, 375, 600, 100))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        state = 1
                        break
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if e.pos[0] in range(400, 1000):
                            if e.pos[1] in range(200, 300):
                                state = 2
                            elif e.pos[1] in range(350, 450):
                                state = 1
                        pygame.draw.circle(screen, pygame.Color('Red'), e.pos, 20)
                        pygame.display.update()
            pygame.display.flip()
            clock.tick(60)

        elif state == 4:
            screen.fill(pygame.Color('Blue'))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        state = 1
                        break
            pass  # TODO:написать меню уровней
            pygame.display.flip()
            clock.tick(60)

        elif state == 5:
            screen.fill((0, 0, 0))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        state = 1
                        break
            pass  # TODO:написать титры
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()

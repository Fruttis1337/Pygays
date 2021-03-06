import pygame
from pygame import *
from GameWorld import World
from Coin import Coin
from Platform import Platform
from Enemy import Enemy, Boss
from MainHero import Hero

WIN_WIDTH = 1400
WIN_HEIGHT = 900

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_capture = 'Game'
    bg_image = pygame.image.load('background.jpg')
    game = True
    playerSave = tuple(open('save.txt').readline().split())  # файл сохранения игры
    lastlvl = playerSave[0]  # Последний пройденный уровень
    playerMoney = playerSave[1]  # Сохраненное кол-во денег
    level = open('level1.txt')
    bx, by = list(map(int, level.readline().split()))
    plats = []
    cns = []
    enm = []
    bs = []
    state = 1  # 1 - меню, 2 - игра, 3 - смерть, 4 - уровни, 5 - титры, 6 - пауза, 7 - уровень пройден


    while game:
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
                                phr = level.readline().split()  # считываем уровень
                                hero = Hero(int(phr[0]), int(phr[1]))
                                phr = level.readline().split()
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
                                world = World([hero], plats, cns, enm, bs)  # конец считывания уровня
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
                        state = 6
                        break
            for i in world.get_platforms():
                i(screen)
            for i in world.get_coins():
                i(screen)
            for i in world.get_enemies():
                i(screen)
            for i in world.get_boss():
                i(screen)
            world.mainhero[0](screen)
            # TODO:взаимодействия с кнопками и игроком

            world.check_coins(world.mainhero[0].get_coords())
            world.check_platform(world.mainhero[0].get_coords())
            world.check_enemies(world.mainhero[0].get_coords())
            world.check_enemies(world.mainhero[0].get_coords())
            pygame.display.flip()
            clock.tick(60)
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
                                phr = level.readline().split()  # считываем уровень
                                hero = Hero(int(phr[0]), int(phr[1]))
                                phr = level.readline().split()
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
                                world = World([hero], plats, cns, enm, bs)  # конец считывания уровня
                                state = 2
                                break
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
        elif state == 6:
            f2 = pygame.font.SysFont('serif', 48)
            txt = f2.render('ПАУЗА', 1, (0, 0, 0))
            txt1 = f2.render('Меню', 1, (255, 255, 255))
            pygame.draw.rect(screen, pygame.Color('Black'), (400, 350, 600, 100))
            screen.blit(txt1, (625, 375, 600, 100))
            screen.blit(txt, (625, 225, 600, 100))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if e.pos[0] in range(400, 1000):
                            if e.pos[1] in range(350, 450):
                                state = 1
                        pygame.draw.circle(screen, pygame.Color('Red'), e.pos, 20)
                        pygame.display.update()
                if e.type == KEYDOWN:
                    state = 2
                    break
            pygame.display.flip()
            clock.tick(60)
        elif state == 7:
            # TODO: вставить кат-сцены
            pass  # TODO: перезаписать сохранение и лок.переменные
            f2 = pygame.font.SysFont('serif', 48)
            txt1 = f2.render('Меню', 1, (255, 255, 255))
            txt2 = f2.render('Следующий уровень', 1, (255, 255, 255))
            screen.fill(pygame.Color('Pink'))
            pygame.draw.rect(screen, pygame.Color('Black'), (100, 700, 500, 100))
            pygame.draw.rect(screen, pygame.Color('Black'), (800, 700, 500, 100))
            screen.blit(txt1, (275, 725, 400, 100))
            screen.blit(txt2, (825, 725, 400, 100))
            for e in pygame.event.get():
                if e.type == QUIT:
                    game = False
                    break
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        state = 1
                        break
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if e.pos[1] in range(600, 700):
                            if e.pos[0] in range(200, 600):
                                state = 1
                            if e.pos[0] in range(800, 1200):
                                pass  # TODO:переход на след.уровень
                        pygame.draw.circle(screen, pygame.Color('Red'), e.pos, 20)
                        pygame.display.update()
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()

import pygame  # TODO: изменить под World полностью!!!
from pygame import *

STEP_SPEED = 1
MOVE_SPEED = 4
MOVE_EXTRA_SPEED = 3  # ускорение
WIDTH = 50
HEIGHT = 80
COLOR = "#888888"
JUMP_POWER = 8
JUMP_EXTRA_POWER = 2  # дополнительная сила прыжка
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class Hero(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.x = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.y = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.isFly = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        self.hp = 3
        self.money = 0

    def get_coords(self):
        return self.x, self.y

    def update(self, left, right, up, running, platforms):

        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
                if running and (left or right):  # если есть ускорение и мы движемся
                    self.yvel -= JUMP_EXTRA_POWER  # то прыгаем выше

        if left:
            if self.xvel < 0:
                self.xvel = -MOVE_SPEED  # Лево = x- n
            else:
                self.xvel = -STEP_SPEED
            if running:  # если усkорение
                self.xvel -= MOVE_EXTRA_SPEED  # то передвигаемся быстрее

        if right:
            if self.xvel > 0:
                self.xvel = MOVE_SPEED
            else:
                self.xvel = STEP_SPEED
            if running:  # если усkорение
                self.xvel += MOVE_EXTRA_SPEED  # то передвигаемся быстрее

        self.image.fill(Color(COLOR))

        if not (left or right) and not self.isFly:  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        if abs(round(self.yvel)) > 2:
            # print("В воздухе")
            self.isFly = True
        elif self.onGround:
            # print "Стоит"
            self.isFly = False

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.x # то не движется вправо
                    self.xvel = 0

                if xvel < 0:  # если движется влево
                    self.rect.left = p.x + p.width  # то не движется влево
                    self.xvel = 0

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.y  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.y + p.height  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def __call__(self, *args, **kwargs):
        pygame.draw.rect(args[0], pygame.Color('Green'), (self.x * 50 + 15, self.y * 50, 20, 50))

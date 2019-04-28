import pygame #TODO: изменить под World полностью!!!
from pygame import *

GRAVITY = 0.35


class Hero(sprite.Sprite):
    def __init__(self, x, y, state=None, *groups):
        sprite.Sprite.__init__(self)
        self.hp = 3
        self.x = x
        self.y = y
        self.state = state
        self.weapon = False
        self.x = 0
        self.y_velocity = 0
        self.on_ground = True
        self.image = Surface((32, 64))
        self.rect = pygame.Rect((0, 0, 32, 64))

    def move(self, left=False, right=False, up=False):
        if left:
            self.rect.x -= 1
            return
        if right:
            self.rect.x += 1
            return
        if up:
            if self.on_ground:
                self.y_velocity = -5
            if not self.on_ground:
                self.y_velocity += GRAVITY
            self.on_ground = True  # TODO: change this line
            self.rect.y += self.y_velocity

    def draw(self, screen):
        pygame.draw.rect(self.rect.x, self.rect.y, )
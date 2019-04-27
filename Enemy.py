import pygame as pg


class Enemy:
    def __init__(self, x, y):
        self.alive = True
        self.health = 3
        self.startx = x
        self.starty = y

    def get_coords(self):
        return self.x, self.y

    def get_state(self):
        return self.health


class FSO(Enemy):
    def __init__(self):
        self.angry = 3
        super().__init__(x, y)

    def get_state(self):
        return self.health, self.angry

    def give_gun(self, a):
        if a == 1:
            return 1
        else:
            return 0

    def soft_touch(self):
        self.angry -= self.angry
        if self.angry == 0:
            return self.give_gun(int(input('Do you want the gun?')))

    def hero_run_from_me(self):
        self.angry += self.angry
        if self.angry >= 5:


    def dogovor(self, other):
        other.coins -= 4



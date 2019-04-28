import pygame as pg


class Enemy:
    def __init__(self, x, y):
        self.alive = True
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def get_state(self):
        return self.health

    def __call__(self, *args, **kwargs):
        import pygame as pg
        pg.draw.rect(args[0], pg.Color('Blue'), (self.x * 20, self.y * 20, 20, 20))


class FSO(Enemy):
    def __init__(self, x, y):
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

    def hero_run_from_me(self, others):
        self.angry += self.angry
        if self.angry >= 5:
            others.damage

    def dogovor(self, other):
        other.coins -= 4


class Boss(Enemy):
    def __init__(self, x, y):
        self.health = 10
        super.__init__(x, y)

    def damage(self):
        self.health -= 1

    def __call__(self, *args, **kwargs):
        import pygame as pg
        pg.draw.rect(args[0], pg.Color('Red'), (self.x * 20, self.y * 20, 20, 20))

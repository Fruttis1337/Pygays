class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_taken = False

    def take(self, coords):
        if coords == self.get_coords():
            self.is_taken = True

    def get_coords(self):
        return self.x, self.y #кортеж

    def get_state(self):
        return self.is_taken

    def __call__(self, *args, **kwargs):
        import pygame as pg
        pg.draw.rect(args[0], pg.Color('Yellow'), (self.x * 20, self.y * 20, 20, 20))

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
class World:
    def __init__(self, mainhero = [], platforms=[], coins=[], enemies=[], boss=[]):
        self.mainhero = mainhero
        self.platforms = platforms
        self.coins = coins
        self.enemies = enemies
        self.boss = boss

    def check_mainhero(self):
        pass

    def check_platform(self, coords):
        for i in self.platforms:
            if i.get_coords == coords:
                i.start_count = True
            if i.get_state():
                i.lower_time()
        filter(lambda x: x.is_broken(), self.platforms)

    def check_coins(self, coords):
        for i in self.coins:
            i.take(coords)
            self.mainhero[0].money += 1
        filter(lambda x: not x.is_taken, self.platforms)

    def check_enemies(self, coords):
        for i in self.enemies:
            if coords == i.get_coords:
                pass #вызвать консоль выбора
        filter(lambda x: x.get_state(), self.enemies)

    def check_boss(self, coords):
        for i in self.boss:
            if coords == i.get_coords:
                pass #наносится урон игроку
            if not i.get_state():
                self.boss = []

    def get_platforms(self):
        return self.platforms

    def get_coins(self):
        return self.coins

    def get_enemies(self):
        return self.enemies

    def get_boss(self):
        return self.boss

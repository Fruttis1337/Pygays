class World:
    def __init__(self, platforms=[], coins=[], enemies=[], boss=None):
        self.platforms = platforms
        self.coins = coins
        self.enemies = enemies
        self.boss = boss

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
        filter(lambda x: not x.is_taken, self.platforms)

    def check_enemies(self, coords):
        for i in self.enemies:
            if coords == i.get_coords:
                pass #вызвать консоль выбора
        filter(lambda x: x.get_state(), self.enemies)

    def check_boss(self, coords):
        if self.boss is not None:
            if coords == self.boss.get_coords:
                pass #наносится урон игроку
        if not self.boss.get_state():
            self.boss = None


    def get_platforms(self):
        return [i.get_coords() for i in self.platforms]

    def get_coins(self):
        return [i.get_coords() for i in self.coins]

    def get_enemies(self):
        return [i.get_coords() for i in self.enemies]

    def get_boss(self):
        return self.boss.get_coords()
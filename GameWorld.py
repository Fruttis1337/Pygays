class World:
    def __init__(self, platforms=[], coins=[], enemies=[], boss=[]):
        self.platforms = platforms
        self.coins = coins
        self.enemies = enemies
        self.boss = boss

    def check_platform(self):
        for i in self.platforms:
            if i.get_type:
                i.lower_time()
        filter(lambda x: x.is_broken(), self.platforms)

    def check_coins(self):
        for i in self.coins:
            i.take()
        filter(lambda x: x.is_taken, self.platforms)

    def check_enemies(self):
        pass #сами делайте

    def check_boss(self):
        pass #и это тоже

    def get_platforms(self):
        return [i.get_coords() for i in self.platforms]

    def get_coins(self):
        return [i.get_coords() for i in self.coins]

    def get_enemies(self):
        return [i.get_coords() for i in self.enemies]

    def get_boss(self):
        return [i.get_coords() for i in self.boss]

class Platform:
    def __init__(self, x, y, state, time=5):
        self.x = x
        self.y = y
        self.type = state
        self.time = time
        self.is_broken = False
        self.start_count = False

    def get_state(self):
        return self.is_broken

    def get_type(self):
        return self.type

    def get_state(self):
        return self.start_count

    def get_coords(self):
        return self.x, self.y

    def lower_time(self):
        self.time -= 1
        if not self.time:
            self.is_broken = True
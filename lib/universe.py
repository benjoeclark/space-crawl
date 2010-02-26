import player
import random

class Universe:
    def __init__(self):
        self.player = player.Player()
        self.galaxy = Galaxy()


class Galaxy:
    def __init__(self):
        self.bodies = []
        self.range = 10
        for count in xrange(random.randint(10, 20)):
            x, y = self.generate_position()
            self.bodies.append(Planet(x, y))

    def generate_position(self):
        x, y = None, None
        while not self.is_valid_position(x, y):
            x = random.randint(-self.range/2, self.range/2)
            y = random.randint(-self.range/2, self.range/2)
        return x, y

    def is_valid_position(self, x, y):
        if x is None or y is None:
            return False
        for body in self.bodies:
            if x == body.x and y == body.y:
                return False
        return True

class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

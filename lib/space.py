import player
import ship
import circle
import random

class Universe:
    def __init__(self):
        self.player = player.Player(ship=ship.Pod())
        self.galaxy = Galaxy()

    def detect_collision(self):
        collisions = []
        for body in self.galaxy.bodies:
            if body.x == self.player.x and body.y == self.player.y:
                collisions.append(body)
        return collisions


class Galaxy:
    def __init__(self):
        self.bodies = []
        self.range = 50
        for count in xrange(random.randint(10, 20)):
            x, y = self.generate_position()
            self.bodies.append(Planet(x, y))
        for count in xrange(random.randint(5, 10)):
            x, y = self.generate_position()
            self.bodies.append(player.Npc(x, y, '!', 'enemy', ship.Pod()))

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
    def __init__(self, x, y, symbol='o', name='planet'):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.radius = random.randint(3, 8)
        self.generate_image()

    def generate_image(self):
        self.image = circle.Circle(self.radius, '*').get_circle_strings()

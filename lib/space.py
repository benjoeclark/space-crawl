import player
import ship
import circle
import random

class Universe:
    def __init__(self, user):
        self.generate_universe()
        self.player = user

    def generate_universe(self, height=23, width=79):
        self.height, self.width = height, width
        self.positions = []
        for x in range(1, self.height):
            for y in range(self.width):
                self.positions.append([x, y])
        self.galaxy_positions = []
        self.galaxy_positions.append(self.pull_position([(self.height-1)/2-1,
                                                self.width/2]))
        self.galaxy_positions.append(self.pull_position([(self.height-1)/2+2,
                                                self.width/2]))
        self.paths = []
        self.paths.append(self.pull_position([(self.height-1)/2,
                                                self.width/2]))
        self.paths.append(self.pull_position([(self.height-1)/2+1,
                                                self.width/2]))
        for galaxy_count in range(20):
            base_galaxy = random.choice(self.galaxy_positions)
            position = self.get_possible_position(base_galaxy)
            if position is not None:
                self.galaxy_positions.append(self.pull_position(position))
                self.get_paths(base_galaxy, self.galaxy_positions[-1])
        self.galaxies = []
        for index in range(len(self.galaxy_positions)):
            self.galaxies.append(Galaxy(self.galaxy_positions[index], self.get_danger(index)))

    def get_danger(self, index):
        return int(10./len(self.galaxy_positions) * index)

    def get_paths(self, base, remote):
        for x in range(base[0]+1, remote[0]):
            if [x, base[1]] in self.positions:
                self.paths.append(self.pull_position([x, base[1]]))
        for x in range(remote[0]+1, base[0]):
            if [x, base[1]] in self.positions:
                self.paths.append(self.pull_position([x, base[1]]))
        for y in range(base[1]+1, remote[1]):
            if [base[0], y] in self.positions:
                self.paths.append(self.pull_position([base[0], y]))
        for y in range(remote[1]+1, base[1]):
            if [base[0], y] in self.positions:
                self.paths.append(self.pull_position([base[0], y]))

    def get_possible_position(self, base):
        possible = []
        up = ([base[0]-1, base[1]] not in self.paths) and \
            ([base[0]-1, base[1]] not in self.galaxy_positions)
        for x in range(base[0]-2, 0, -1):
            if up:
                if [x, base[1]] in self.positions:
                    possible.append([x, base[1]])
                else:
                    up = False
        down = ([base[0]+1, base[1]] not in self.paths) and \
            ([base[0]+1, base[1]] not in self.galaxy_positions)
        for x in range(base[0]+2, 24):
            if down:
                if [x, base[1]] in self.positions:
                    possible.append([x, base[1]])
                else:
                    down = False
        left = ([base[0], base[1]-1] not in self.paths) and \
            ([base[0], base[1]-1] not in self.galaxy_positions)
        for y in range(base[1]-2, -1, -1):
            if left:
                if [base[0], y] in self.positions:
                    possible.append([base[0], y])
                else:
                    left = False
        right = ([base[0], base[1]+1] not in self.paths) and \
            ([base[0], base[1]+1] not in self.galaxy_positions)
        for y in range(base[1]+2, 80):
            if right:
                if [base[0], y] in self.positions:
                    possible.append([base[0], y])
                else:
                    right = False
        if len(possible) == 0:
            return None
        return random.choice(possible)

    def pull_position(self, position):
        return self.positions.pop(self.positions.index(position))

    def detect_collision(self):
        collisions = []
        for body in self.galaxy.bodies:
            if body.x == self.player.x and body.y == self.player.y:
                collisions.append(body)
        return collisions


class Galaxy:
    def __init__(self, position, danger):
        self.bodies = []
        self.position = position
        self.danger = danger
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

import player
import ship
import circle
import random
import math

class Galaxy:
    def __init__(self, user, maxx=7, maxy=26, systems_count=25):
        self.player = user
        self.maxx = maxx
        self.maxy = maxy
        self.system_names = ['Milky Way',
                            'Andromeda',
                            'Onyx',
                            'Ferven',
                            'Lost',
                            'Calden',
                            'Numen',
                            'Anden',
                            'Eden',
                            'Tlord',
                            'Quard',
                            'Pnid',
                            'Fra',
                            'Vim',
                            'Xranut',
                            'Tindar',
                            'Bith',
                            'Ion',
                            'Wanrd',
                            'Mined',
                            'Descrid',
                            'Zinf',
                            'Pluntis',
                            'Sasc',
                            'Eon']
        self.systems = []
        for counter in xrange(systems_count):
            self.systems.append(System(self.get_system_name(),
                            self.generate_position()))
        self.player.starting_base(self.systems[0])

    def propagate(self, dt):
        self.player.propagate(dt)
        for system in self.systems:
            system.propagate(dt)

    def get_system_name(self):
        index = random.randint(0, len(self.system_names)-1)
        return self.system_names.pop(index)

    def generate_position(self):
        position = None
        while not self.is_valid_position(position):
            x = random.randint(0, self.maxx-1)
            y = random.randint(0, self.maxy-1)
            position = [x, y]
        return position

    def is_valid_position(self, position):
        if position is None:
            return False
        for system in self.systems:
            if position[0] == system.position[0] and \
                position[1] == system.position[1]:
                return False
        return True


class System:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.radius = random.randint(5, 8)
        self.astrals = []
        self.astrals.append(Star(self.generate_position(2)))
        for planet_count in xrange(random.randint(5, 9)):
            self.astrals.append(Planet(self.generate_position()))

    def propagate(self, dt):
        for astral in self.astrals:
            astral.propagate(dt)

    def generate_position(self, radius=None):
        position = None
        while not self.is_valid_position(position):
            angle = random.randint(0, 359)
            radial = random.randint(2,
                self.radius if radius is None else radius)
            position = [int(radial*math.sin(angle*math.pi/180.)),
                        int(radial*math.cos(angle*math.pi/180.))]
        return position

    def is_valid_position(self, position):
        if position is None:
            return False
        for astral in self.astrals:
            if position[0] == astral.position[0] and \
                position[1] == astral.position[1]:
                return False
        return True


class Astral(object):
    def __init__(self, position, name=None):
        self.position = position
        self.name = name
        self.symbol = '*'
        self.initialize()

    def initialize(self):
        pass

    def propagate(self, dt):
        pass


class Star(Astral):
    pass


class Planet(Astral):
    def initialize(self):
        self.symbol = 'o'
        self.resources = []

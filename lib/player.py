class Commander(object):
    def __init__(self, faction):
        self.faction = faction
        self.system = None
        self.fleets = [Fleet()]

    def set_system(self, system):
        self.system = system


class Player(Commander):
    pass


class Fleet(object):
    def __init__(self, name='Base'):
        self.name = name


class Pilot(object):
    def __init__(self, x=0, y=0, symbol='@', name='Player', ship=None):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.name = name
        self.ship = ship

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class PilotPlayer(Pilot):
    pass

class Npc(Pilot):
    pass

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

class Player(Pilot):
    pass

class Npc(Pilot):
    pass

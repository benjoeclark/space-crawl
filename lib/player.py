class Pilot:
    def __init__(self, x=0, y=0, symbol='@'):
        self.x = x
        self.y = y
        self.symbol = symbol

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Player(Pilot):
    pass

class Npc(Pilot):
    pass

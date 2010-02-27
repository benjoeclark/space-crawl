"""state

Module to handle various game states"""

from universe import Universe

class State:
    """State superclass"""
    def __init__(self, screen, universe=None):
        """Generic class initialization"""
        self.screen = screen
        self.universe = universe if universe is not None else Universe()
        self.start()

    def start(self):
        """Initialization function to be implemented in the subclass"""
        pass


class New(State):
    def start(self):
        """Welcome the user and start a new game"""
        self.screen.clear()
        self.screen.addstr(0, 0, 'Welcome to MW10')
        self.screen.addstr(1, 0, 'press any key to launch into the unknown')

    def handle_key(self, key):
        """On any keypress, launch the ship"""
        self.screen.clear()
        return Flight(self.screen, self.universe)


class Flight(State):
    def start(self):
        self.show_galaxy()

    def handle_key(self, key):
        if key == ord('k'):
            self.universe.player.move(-1, 0)
        elif key == ord('j'):
            self.universe.player.move(1, 0)
        elif key == ord('h'):
            self.universe.player.move(0, -1)
        elif key == ord('l'):
            self.universe.player.move(0, 1)
        self.screen.clear()
        collision = self.universe.detect_collision()
        if collision is not None:
            self.screen.addstr(0, 0, 'collision detected')
        self.show_galaxy()

    def show_galaxy(self):
        height, width = self.screen.getmaxyx()
        self.screen.addstr(height/2, width/2, self.universe.player.symbol)
        for body in self.universe.galaxy.bodies:
            x, y = self.relative_position(body, self.universe.player)
            x += height/2
            y += width/2
            if x < 1:
                x = 1
            elif x >= height-2:
                x = height-2
            if y < 1:
                y = 1
            elif y >= width-2:
                y = width-2
            self.screen.addstr(x, y, body.symbol)

    def relative_position(self, body, player):
        return body.x - player.x, body.y - player.y

"""game.py

This module contains the handlers for the mw10 game"""

import threading
import time
import curses
import universe
import player
import display
import galaxyselection
import dock
import orbit
import flight

class Input(threading.Thread):
    """Class for handling getting input from the user and acting on it"""
    def __init__(self, game):
        """Initialize the input thread, keeping track of the game"""
        self.game = game
        threading.Thread.__init__(self)

    def run(self):
        """Run the input thread to wait for user input"""
        while self.game.running:
            self.game.handle_command(self.game.screen.getch())


class Game:
    """The class to handle actions for the game"""
    def __init__(self, fps=5):
        """Initialize the game by initializing all required variables
        and starting the screen through the class start method"""
        # running variables
        self.fps=fps
        self.running = True
        self.state = 0
        # game classes
        self.universe = universe.Universe()
        self.player = player.Player()
        curses.wrapper(self.start)

    def start(self, screen):
        """Start the game with the included screen by starting the game
        threads"""
        curses.curs_set(0) #Make the cursor invisible
        curses.raw()
        self.screen = screen
        Input(self).start()
        while self.running:
            self.show_state()
            time.sleep(1./self.fps)

    def show_state(self):
        """Show the current game state"""
        self.screen.clear()
        self.move()
        self.screen.addstr(1, 1, str(self.player.position[1]))
        self.screen.addstr(2, 1, str(self.player.velocity))
        self.screen.addstr(3, 1, str(self.player.thrust))
        self.screen.addstr(4, 1, str(self.state))
        self.screen.refresh()

    def move(self):
        """Call the move command for all mobile objects"""
        self.player.move(1./self.fps)

    def handle_command(self, ch):
        """Handle the command from the user"""
        if ch == 27:
            self.running = False
        elif ch == ord('w'):
            self.player.change_thrust(10)
        elif ch == ord('s'):
            self.player.change_thrust(-10)
        else:
            self.state = ch

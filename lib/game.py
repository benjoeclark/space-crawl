"""game.py

This module starts and tracks the MW10 game"""

import curses
import player
import universe
import state

class Game:
    """Main game class"""
    def __init__(self):
        """Start the game through curses"""
        curses.wrapper(self.start)

    def start(self, screen):
        """Initialize the game"""
        self.running = True
        self.player = player.Player()
        self.universe = universe.Universe()
        self.state = [state.Launched()]
        self.screen = screen.subwin(23, 79, 0, 0)
        curses.raw()
        curses.curs_set(0) # make the cursor invisible
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            key = self.screen.getch()
            if key == 27:
                self.running = False
            else:
                self.state[0].handle_key(key)
            self.screen.clear()
            self.screen.addstr(0, 0, str(key))
            self.screen.refresh()

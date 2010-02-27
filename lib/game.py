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
        self.universe = universe.Universe()
        self.ui = screen
        self.screen = screen.subwin(23, 79, 0, 0)
        curses.raw()
        curses.curs_set(0) # make the cursor invisible
        self.state = state.New(self.screen)
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            key = self.ui.getch()
            if key == 27:
                self.running = False
            else:
                next_state = self.state.handle_key(key)
                if next_state is not None:
                    self.state = next_state
            self.screen.addstr(22, 0, str(key))
            self.screen.refresh()

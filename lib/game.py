"""game.py

This module starts and tracks the MW10 game"""

import curses

class Game:
    """Main game class"""
    def __init__(self):
        """Start the game through curses"""
        curses.wrapper(self.start)

    def start(self, screen):
        """Initialize the game"""
        self.running = True
        self.screen = screen
        curses.raw()
        curses.curs_set(0) # make the cursor invisible
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            key = self.screen.getch()
            if key == 27:
                self.running = False
            self.screen.clear()
            self.screen.addstr(0, 0, str(key))
            self.screen.refresh()

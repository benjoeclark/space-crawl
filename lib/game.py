"""game.py

This module starts and tracks the MW10 game"""

import curses
import state
import time

class Game:
    """Main game class"""
    def __init__(self, fps=10.):
        """Start the game through curses"""
        self.fps = fps
        curses.wrapper(self.start)

    def start(self, screen):
        """Initialize the game"""
        self.running = True
        self.ui = screen
        self.ui.timeout(0)
        self.screen = screen.subwin(23, 79, 0, 0)
        curses.raw()
        #curses.curs_set(0) # make the cursor invisible
        self.state = state.New(self.screen)
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            time.sleep(1./self.fps)
            key = self.ui.getch()
            if key == -1:
                pass
            elif key == 27:
                self.running = False
            else:
                next_state = self.state.handle_key(key)
                if next_state is not None:
                    self.state = next_state
            self.state.show()

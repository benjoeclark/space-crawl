"""game.py

This module starts and tracks the MW10 game"""

import curses
import state
import space
import cPickle

class Game:
    """Main game class"""
    def __init__(self):
        """Start the game through curses"""
        curses.wrapper(self.start)

    def start(self, screen):
        """Initialize the game"""
        self.running = True
        self.ui = screen
        self.screen = screen.subwin(23, 79, 0, 0)
        #try:
        #    save_file = open('mw10.save', 'r')
        #    self.universe = cPickle.load(save_file)
        #except:
        #    self.universe = space.Universe()
        self.universe = space.Universe()
        curses.raw()
        curses.curs_set(0) # make the cursor invisible
        self.state = state.GalaxySelector(self.screen, self.universe)
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            key = self.ui.getch()
            if key == 27:
                self.running = False
                self.save()
            else:
                next_state = self.state.handle_key(key)
                if next_state is not None:
                    self.state = next_state
            self.screen.refresh()

    def save(self):
        save_file = open('mw10.save', 'w')
        cPickle.dump(self.universe, save_file)
        save_file.close()

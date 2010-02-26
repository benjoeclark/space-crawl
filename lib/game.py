"""game.py

This module starts and tracks the MW10 game"""

import ui

class Game:
    """Main game class"""
    def __init__(self):
        """Initialize and start the game"""
        self.log = open('log', 'w')
        self.input = ui.Input()
        self.screen = ui.Screen()
        self.running = True
        self.run()
        self.log.close()

    def run(self):
        """Main game loop"""
        while self.running:
            key = self.input()
            self.log.write(str(ord(key)) + '\n')
            if ord(key) == 27:
                self.running = False
            self.screen.message(key)
            self.screen.flip()

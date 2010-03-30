"""game.py

This module starts and tracks the MW10 game"""

import time
import screen
import state

class Game:
    """Main game class"""
    def __init__(self):
        """Initialize the game"""
        self.running = True
        self.screen = screen.Screen()
        self.state = state.New(self.screen)
        self.run()

    def run(self):
        """Main game loop"""
        while self.running:
            now = time.time()
            self.screen.draw()
            command = raw_input()
            self.running = self.handle_command(command)
            self.state.propagate(time.time() - now)
        self.screen.addstr(-1, 0, 'Goodbye')
        self.screen.draw()

    def handle_command(self, command):
        if command == 'exit':
            return False
        elif command == 'galaxy':
            self.state = state.GalaxyView(self.state.screen, self.state.galaxy)
        elif len(command) == 1 and command.isdigit():
            try:
                fleet = self.state.galaxy.player.fleets[int(command)]
                self.state = state.FleetView(self.state.screen,
                                            self.state.galaxy,
                                            fleet)
            except IndexError:
                pass
        else:
            new_state = self.state.handle_command(command)
            if new_state is not None:
                self.state = new_state
        return True

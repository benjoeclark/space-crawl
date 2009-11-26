#!/usr/bin/env python

import universe
import player
import display

class Game:
    """The game class to handle the background actions for playing mw10"""
    def __init__(self, display_type):
        """Initialize a game"""
        self.game_running = True
        self.state = 'select'
        self.universe = universe.Universe()
        self.player = player.Player()
        self.display = display.TextDisplay(self, debug=True)
        self.start()

    def start(self):
        """Start a new game"""
        self.display.show_state()
        self.run()

    def run(self):
        """Run the game (main loop)"""
        while self.game_running:
            command = self.display.get_user_input()
            self.handle_command(command)
            self.display.show_state()

    def introduction(self):
        """Game startup introduction"""
        return 'You have been chosen as captain of a colony sent to Milky Way 10'

    def get_state(self):
        """Get the current state"""
        return self.state

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'help':
            self.state = 'help'
        elif command == 'quit':
            self.state = 'quit'
            self.game_running = False
        elif command == 'galaxy':
            self.state = 'galaxy'
    
    def get_galaxy_names(self):
        """Get the galaxy names in the universe"""
        return self. universe.get_galaxy_names()

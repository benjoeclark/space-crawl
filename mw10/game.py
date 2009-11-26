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
        self.display = display.TextDisplay()
        self.start()

    def start(self):
        """Start a new game"""
        sprites = self.get_introduction()
        sprites.extend(self.universe.galaxies)
        self.display.set_prompt(self.get_prompt())
        self.display.set_sprites(sprites)
        self.display.draw()
        self.run()

    def get_introduction(self):
        """Game startup introduction"""
        introduction = ['You have been chosen as captain of a colony',
                'sent to Milky Way 10',
                'Select a starting galaxy:']
        introduction.extend(self.universe.get_galaxy_names())
        return introduction

    def run(self):
        """Run the game (main loop)"""
        while self.game_running:
            command = self.display.get_user_input()
            self.handle_command(command)
            self.display.draw()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'help':
            self.display.set_sprites(self.help_menu())
        elif command == 'quit':
            self.display.set_sprites(self.game_over())
            self.game_running = False
        elif command == 'galaxy':
            self.state = 'galaxy'

    def help_menu(self):
        """Display the game's text help menu"""
        buffer = ['Help for mw10:',
                '    command        description',
                '    -------        -----------',
                '    quit           exit the game']
        return buffer
    
    def game_over(self):
        """Display a game over sign"""
        buffer = ['Goodbye for now']
        return buffer

    def get_state(self):
        """Get the current state"""
        return self.state

    def get_galaxy_names(self):
        """Get the galaxy names in the universe"""
        return self.universe.get_galaxy_names()

    def get_prompt(self):
        """Get the customizable prompt string"""
        return '@MW10 $'

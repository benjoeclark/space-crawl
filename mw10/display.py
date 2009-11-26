#!/usr/bin/env python

import actions
import os

class TextDisplay:
    """Display for playing MW10 in a console"""
    def __init__(self, game, debug=False):
        """Initialize a TextDisplay"""
        self.width = 21
        self.height = 21
        self.game = game
        self.debug = debug

    def start(self, introduction):
        """Show the introduction to start the game"""
        print introduction

    def show_state(self):
        """Display the current state of the game, depending on what
        screen is currently in view"""
        self.clear()
        if self.game.get_state() == 'help':
            self.help()
        elif self.game.get_state() == 'quit':
            self.game_over()
        elif self.game.get_state() == 'select':
            self.select()
        else:
            print 'Current system state'

    def select(self):
        """Show the galaxy selection screen"""
        buffer = ['Select a starting galaxy:']
        for galaxy_name in self.game.get_galaxy_names():
            buffer.append('    ' + galaxy_name)
        print self.fill_screen(buffer)

    def inform(self, message):
        """Inform the user of the message"""
        print message

    def get_user_input(self):
        """Wait for the user input, and return an action based on it"""
        command = raw_input(self.prompt())
        return command

    def prompt(self):
        """Get the customizable prompt string"""
        return '@MW10 $'

    def fill_screen(self, buffer=[]):
        """Fill a screen given a set of lines, used for displaying lines
        of text"""
        output = ''
        if len(buffer) < self.height:
            for line in buffer:
                output += line + '\n'
            output += '\n'*(self.height - len(buffer) - 1)
        return output

    def help(self):
        """Display the game's text help menu"""
        buffer = ['Help for mw10:',
                '    command        description',
                '    -------        -----------',
                '    quit           exit the game']
        print self.fill_screen(buffer)

    def game_over(self):
        """Display a game over sign"""
        buffer = ['Goodbye for now']
        print self.fill_screen(buffer)

    def clear(self):
        """Clear the screen if not in debug mode"""
        if not self.debug:
            os.system('clear')

#!/usr/bin/env python

import actions
import os

class TextDisplay:
    """Display for playing MW10 in a console"""
    def __init__(self, state, debug=False):
        """Initialize a TextDisplay"""
        self.state = state
        self.debug = debug

    def show_state(self):
        """Display the current state of the game, depending on what
        screen is currently in view"""
        self.clear()
        if self.state.get_state() == 'help':
            self.help()
        else:
            print 'Current system state'

    def inform(self, message):
        """Inform the user of the message"""
        print message

    def get_user_input(self):
        """Wait for the user input, and return an action based on it"""
        command = raw_input(self.prompt())
        if command == 'quit':
            requested_action = actions.Quit()
        elif command == 'help':
            requested_action = actions.Help()
        else:
            requested_action = actions.Action()
        return requested_action

    def prompt(self):
        """Get the customizable prompt string"""
        return '@MW10 $'

    def game_over(self):
        """Display a game over sign"""
        self.clear()
        print 'Goodbye for now'

    def help(self):
        """Display the game's text help menu"""
        print 'Help for mw10:\n\tcommand\t\tdescription\n\tquit\t\texit the game'

    def clear(self):
        """Clear the screen if not in debug mode"""
        if not self.debug:
            os.system('clear')

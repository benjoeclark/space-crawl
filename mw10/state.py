#!/usr/bin/env python

import actions

class State:
    """Current game state class"""
    def __init__(self):
        """Initialize the game state"""
        self.view_state = ''

    def act(self, action):
        """Perform the action, return false if quit requested"""
        if isinstance(action, actions.Quit):
            return False
        elif isinstance(action, actions.Help):
            self.view_state = 'help'
        return True

    def get_state(self):
        """Get the current state"""
        return self.view_state

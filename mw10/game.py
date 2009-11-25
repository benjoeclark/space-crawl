#!/usr/bin/env python

import universe
import display
import state
import actions

class Game:
    """The game class to handle the background actions for playing mw10"""
    def __init__(self, display_type):
        """Initialize a game"""
        self.game_running = True
        self.universe = universe.Universe()
        self.state = state.State()
        self.display = display.TextDisplay(self.state, debug=True)
        self.start()

    def start(self):
        """Start a new game"""
        self.display.inform(self.introduction())
        self.run()

    def run(self):
        """Run the game (main loop)"""
        while self.game_running:
            self.display.show_state()
            action = self.display.get_user_input()
            self.game_running = self.state.act(action)
        self.display.game_over()

    def introduction(self):
        """Game startup introduction"""
        return 'You have been chosen as captain of a colony sent to Milky Way 10'

#!/usr/bin/env python

class Action:
    """Superclass for all actions"""
    def __init__(self):
        """Action initialization"""
        pass

class Quit(Action):
    """Quit the game"""
    def __init__(self):
        """Create a quit game instance"""
        pass

class Help(Action):
    """Ask for help"""
    def __init__(self):
        """Create a help instance"""
        pass

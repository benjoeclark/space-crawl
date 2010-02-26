"""ui.py

Module for handling user interface including keyboard and screen"""

import os

class Input:
    """Class for handling user input"""
    def __init__(self):
        """Get the getch function"""
        import getch
        self.getch = getch.getch

    def __call__(self):
        """Call the getch function"""
        return self.getch()


class Screen:
    """Class for handling display of information
    throughout the module, the corner of the screen is located at
    the bottom right"""
    def __init__(self, width=80, height=24):
        """Initialize the screen with a width and height"""
        self.width = width
        self.height = height
        self.buffer = None
        self.clear()
        self.flip()

    def clear(self):
        """Clear the screen"""
        self.buffer = ['*' * self.width] * self.height

    def flip(self):
        os.system('clear')
        buffer_copy = self.buffer[:]
        buffer_copy.reverse()
        print '\n'.join(buffer_copy)

    def message(self, string):
        self.clear()
        self.buffer[0] = string + self.buffer[0][len(string):]

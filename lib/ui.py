"""ui.py

Module for handling user interface including keyboard and screen"""

class Ui:
    """Main user interface class"""
    def __init__(self):
        """Set up parts of the user interface"""
        self.input = Input()
        self.screen = Screen()


class Input:
    """Class for handling user input"""
    def __init__(self):
        """Get the getch function"""
        import getch
        self.getch = getch.getch


class Screen:
    """Class for handling display of information
    throughout the module, the corner of the screen is located at
    the bottom right"""
    def __init__(self, width=80, height=24):
        """Initialize the screen with a width and height"""
        self.width = width
        self.heigh = height

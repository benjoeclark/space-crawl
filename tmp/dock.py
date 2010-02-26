import subgame

class Dock(subgame.Subgame):
    """The subgame that handles operations while docked"""
    def initialize(self):
        """Initialize the docked subgame"""
        self.show_dock()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'launch':
            self.launch()
            self.subgame_running = False

    def show_help(self):
        """Show the help menu"""
        self.game.display.set_sprites(['Help for the dock:',
            '    command        description',
            '    -------        -----------',
            '    launch         leave the dock for space',
            '    quit           exit the game'])

    def show_dock(self):
        """Show the dock"""
        self.game.display.set_sprites(['Welcome to the dock',
            'To leave the dock in your craft, enter launch',
            self.game.player.ship])

    def launch(self):
        """Leave the dock"""
        self.game.player.launch()

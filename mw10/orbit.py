import subgame

class Orbit(subgame.Subgame):
    """The orbit subgame"""
    def initialize(self):
        """Initialize the orbit subgame"""
        self.show_orbit()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'launch':
            self.launch()
            self.subgame_running = False

    def show_help(self):
        """Show the help menu"""
        self.game.display.set_sprites(['Help for the orbit:',
            '    command        description',
            '    -------        -----------',
            '    launch         leave the dock for space',
            '    quit           exit the game'])

    def show_orbit(self):
        """Show the orbit"""
        self.game.display.set_sprites(['Welcome to orbit',
            'To leave orbit, enter launch'])

    def launch(self):
        """Leave orbit"""
        self.game.player.launch()

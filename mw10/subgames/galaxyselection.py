import subgame

class GalaxySelection(subgame.Subgame):
    """The Subgame that handles selecting the starting galaxy"""
    def initialize(self):
        """Initialize the galaxy selection"""
        self.selection = 0
        self.galaxy_list = self.number()
        self.show_selection()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'select':
            self.set_galaxy()
            self.subgame_running = False
        elif self.is_selection(command):
            self.selection = int(command) - 1
            self.show_selection()
        else:
            self.show_selection()

    def show_help(self):
        """Show the help menu"""
        self.game.display.set_sprites(['Help for galaxy selection:',
            '    command        description',
            '    -------        -----------',
            '    select         select the galaxy to start with',
            '    <number>       select the numbered galaxy',
            '    <ENTER>        return to the selection screen',
            '    quit           exit the game'])

    def show_selection(self):
        """Show the current selection"""
        self.game.universe.set_symbols('o')
        self.game.universe.galaxies[self.selection].set_symbol('*')
        buffer = self.get_title()
        buffer.extend(self.mark_selection())
        buffer.extend(self.game.universe.galaxies)
        self.game.display.set_sprites(buffer)

    def get_title(self):
        """Game startup introduction"""
        introduction = ['You have been chosen as captain of a colony',
                'sent to Milky Way 10',
                'Select a starting galaxy:']
        return introduction

    def number(self):
        """Number the galaxies"""
        galaxy_list = self.game.universe.get_galaxy_names()
        return [str(i+1) + ' ' + n for i, n in enumerate(galaxy_list)]

    def mark_selection(self):
        """Mark the currently selected galaxy"""
        marked_list = self.galaxy_list[:]
        marked_list[self.selection] = '*' + marked_list[self.selection][1:]
        return marked_list

    def is_selection(self, command):
        """Check that the command is a valid galaxy selection"""
        try:
            self.game.universe.galaxies[int(command)-1]
        except (ValueError, IndexError):
            return False
        return True

    def set_galaxy(self):
        """Set the galaxy to the current selection"""
        self.game.player.enter_galaxy(
                self.game.universe.galaxies[self.selection])

import universe
import player
import display
from subgames import galaxyselection, dock, flight

class Game:
    """The game class to handle the background actions for playing mw10"""
    def __init__(self, display_type):
        """Initialize a game"""
        self.game_running = True
        self.universe = universe.Universe()
        self.player = player.Player()
        self.display = display.TextDisplay()
        self.display.set_prompt(self.get_prompt())
        self.run()

    def run(self):
        """Run the game, selecting the appropriate subgame to pass off
        focus to"""
        while self.game_running:
            self.select_subgame()

    def select_subgame(self):
        """Select the appropriate subgame to play"""
        if self.player.current_galaxy == None:
            return galaxyselection.GalaxySelection(self)
        elif self.player.docked:
            return dock.Dock(self)
        elif len(self.player.bodies_in_view) > 0:
            return flight.Flight(self)
        else:
            print 'nowhere to go'
            self.game_running = False

    def start(self):
        """Start a new game"""
        sprites = self.get_introduction()
        sprites.extend(self.universe.galaxies)
        self.display.set_prompt(self.get_prompt())
        self.display.set_sprites(sprites)
        self.display.draw()
        self.run()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'help':
            self.display.set_sprites(self.help_menu())
        elif command == 'quit':
            self.display.set_sprites(self.game_over())
            self.game_running = False
        elif command == 'galaxy':
            self.state = 'galaxy'

    def help_menu(self):
        """Display the game's text help menu"""
        buffer = ['Help for mw10:',
                '    command        description',
                '    -------        -----------',
                '    quit           exit the game']
        return buffer
    
    def game_over(self):
        """Display a game over sign"""
        self.game_running = False
        buffer = ['Goodbye for now']
        self.display.set_sprites(buffer)

    def get_state(self):
        """Get the current state"""
        return self.state

    def get_galaxy_names(self):
        """Get the galaxy names in the universe"""
        return self.universe.get_galaxy_names()

    def get_prompt(self):
        """Get the customizable prompt string"""
        return '@MW10 $'

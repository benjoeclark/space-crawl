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
    
    def game_over(self):
        """Display a game over sign"""
        self.game_running = False
        buffer = ['Goodbye for now']
        self.display.set_sprites(buffer)

    def get_prompt(self):
        """Get the customizable prompt string"""
        return '@MW10 $'

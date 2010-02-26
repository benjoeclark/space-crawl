import subgame
import station
import planet

class Flight(subgame.Subgame):
    """Flight subgame for moving around the galaxy"""
    def initialize(self):
        """Initialize the flight subgame"""
        self.show_galaxy()

    def handle_command(self, command):
        """Handle the user command"""
        if command == 'w':
            self.game.player.move((0, 1))
        elif command == 'a':
            self.game.player.move((-1, 0))
        elif command == 's':
            self.game.player.move((0, -1))
        elif command == 'd':
            self.game.player.move((1, 0))
        self.detect_body()
        self.show_galaxy()

    def show_help(self):
        """Show the help menu"""
        self.game.display.set_sprites(['Help for flying:',
            '    command        description',
            '    -------        -----------',
            '    w              move upward',
            '    a              move left',
            '    s              move downward',
            '    d              move right',
            '    <ENTER>        show the galaxy',
            '    quit           exit the game'])

    def show_galaxy(self):
        """Show the current galaxy view"""
        self.game.display.set_sprites(self.game.player.bodies_in_view)

    def detect_body(self):
        """Detect when the player moves over a body"""
        for body in self.game.player.current_galaxy.bodies:
            if self.game.player.position == body.position:
                if isinstance(body, station.Station):
                    self.dock(body)
                elif isinstance(body, planet.Planet):
                    self.orbit(body)

    def dock(self, body):
        """Dock with the detected station"""
        self.game.player.docked = True
        self.game.player.bodies_in_view = []
        self.subgame_running = False

    def orbit(self, body):
        """Orbit the detected planet"""
        self.game.player.orbiting = True
        self.game.player.bodies_in_view = []
        self.subgame_running = False

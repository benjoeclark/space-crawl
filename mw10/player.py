class Player:
    """Class to keep track of the player"""
    def __init__(self):
        """Initialize a player"""
        self.current_galaxy = None
        self.docked = False
        self.bodies_in_view = []
        self.position = None

    def enter_galaxy(self, galaxy):
        """Put the player in the galaxy"""
        self.current_galaxy = galaxy
        self.position = self.current_galaxy.get_station_position()
        self.docked = True

    def launch(self):
        """Leave the dock area"""
        self.docked = False
        self.bodies_in_view = \
                self.current_galaxy.get_bodies_in_view(self.position)

    def move(self, step):
        """Move the player in the given direction"""
        print self.position, step
        self.position = (self.position[0]+step[0], self.position[1]+step[1])
        print self.position
        self.bodies_in_view = \
                self.current_galaxy.get_bodies_in_view(self.position)

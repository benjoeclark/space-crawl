""" player

This module contains the class for keeping track of the player"""

import ship

class Player:
    """Class to keep track of the player"""
    def __init__(self):
        """Initialize a player"""
        self.current_galaxy = None
        self.docked = False
        self.orbiting = False
        self.bodies_in_view = []
        self.position = [0., 0.]
        self.velocity = 0.
        self.thrust = 0
        self.ship = ship.Pod()
        self.contents = []

    def enter_galaxy(self, galaxy):
        """Put the player in the galaxy"""
        self.current_galaxy = galaxy
        self.position = self.current_galaxy.get_station_position()
        self.thrust = 0
        self.docked = True
        self.orbiting = False

    def launch(self):
        """Leave the dock area"""
        self.docked = False
        self.orbiting = False
        self.bodies_in_view = \
                self.current_galaxy.get_bodies_in_view(self.position)

    def get_from_planet(self, planet):
        """Get the contents from the planet"""
        self.contents.append(planet.pop())

    def change_thrust(self, thrust_percent_change):
        """Change the thrust"""
        if 100 > self.thrust and thrust_percent_change > 0:
            self.thrust += thrust_percent_change
        elif 0 < self.thrust and thrust_percent_change < 0:
            self.thrust += thrust_percent_change

    def move(self, dt):
        """Propagate the state over the time interval dt"""
        self.velocity = self.velocity + dt*(self.thrust/100.*self.ship.max_thrust - 1000.*self.velocity)/self.ship.mass
        self.position[1] = self.position[1] + dt*self.velocity
        if self.velocity < 0.0001:
            self.velocity = 0.

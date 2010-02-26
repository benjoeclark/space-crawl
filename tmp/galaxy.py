import random
import math
import planet
import body
import station

class Galaxy:
    """Class to handle keeping up with galaxy elements, including random
    initialization of a galaxy"""
    def __init__(self, position, name='Milky Way 10'):
        """Initialize a galaxy"""
        self.width = 30.
        self.height = 30.
        self.position = position
        self.name = name
        self.symbol = 'O'
        self.bodies = [station.Station(self.generate_position(),
            self.name + ' Station')]
        for index in range(random.randint(5, 10)):
            self.bodies.append(planet.Planet(self.generate_position(),
                str(index)))

    def __repr__(self):
        """String representation of the galazy"""
        return 'galaxy ' + self.name

    def generate_position(self):
        """Get a random position in the galaxy"""
        x = random.uniform(-self.width/2, self.width/2)
        y = random.uniform(-self.height/2, self.height/2)
        return [x, y]

    def get_name(self):
        """Return the galaxy name"""
        return self.name

    def set_symbol(self, symbol):
        """Set the galaxy's map symbol"""
        self.symbol = symbol

    def get_station_position(self):
        """Get the station position, where the player is located after a
        launch"""
        return self.bodies[0].position
    
    def get_bodies_in_view(self, position, radius=10):
        """Get a list of bodies in view of the position"""
        bodies_in_view = []
        for b in self.bodies:
            if self.distance(position, b.position) <= radius:
                bodies_in_view.append(body.Body(
                    self.relative_position(position, b.position),
                    b.name, b.symbol))
        bodies_in_view.append(body.Body((0, 0), 'Player', '^'))
        return bodies_in_view

    def distance(self, user, body):
        """Get the distance between the user and body"""
        relative_position = self.relative_position(user, body)
        return math.sqrt(relative_position[0]**2 + relative_position[1]**2)

    def relative_position(self, user, body):
        """Calculate the position of the body relative to the user"""
        return body[0]-user[0], body[1]-user[1]

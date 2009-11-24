#!/usr/bin/env python

import random
import star

class Galaxy:
    """Class to handle keeping up with galaxy elements, including random
    initialization of a galaxy"""
    def __init__(self):
        """Initialize a galaxy"""
        self.width = 20
        self.height = 20
        self.star = star.Star(self.get_random_location())
        self.name = 'Milky Way 10'

    def __repr__(self):
        """String representation of the galazy"""
        return 'galaxy ' + self.name + ' contains ' + self.star.__repr__()

    def get_random_location(self):
        """Get a random location tuple"""
        return (random.randint(0, self.width-1),
                random.randint(0, self.height-1))

    def get_current_view(self):
        """Returns a string representing the location of items in the
        galaxy"""
        horizontal_border = '|' + '-'*(self.width+2) + '|'
        current_view = horizontal_border + '\n'
        for row in range(self.height):
            current_view += '|'
            if self.star.get_location()[1] == row:
                current_view += ' '*(self.star.get_location()[0])
                current_view += '*'
                current_view += ' '*(self.width+1-self.star.get_location()[0])
            else:
                current_view += ' '*(self.width+2)
            current_view += '|\n'
        current_view += horizontal_border
        current_view += '\n' + str(self.star.get_location())
        return current_view

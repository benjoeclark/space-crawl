#!/usr/bin/env python

import random
import galaxy

class Universe:
    """Class for keeping track of everything in the game universe
    (it's a big job)"""
    def __init__(self):
        """Initalize a new universe"""
        self.possible_galaxy_names = ['Andromeda',
                'Spam',
                'Foo',
                'Bar',
                'B1',
                'B2',
                'B3',
                'B4',
                'B5',
                'B6',
                'F1',
                'F2',
                'F3',
                'F4',
                'F5']
        self.galaxies = []
        for index in range(random.randint(5, 15)):
            self.galaxies.append(galaxy.Galaxy(self.new_name()))
    
    def new_name(self):
        """Get a random galaxy name"""
        return self.possible_galaxy_names.pop(random.randint(0, len(self.possible_galaxy_names)-1))

    def get_galaxy_names(self):
        """Return a list of the galaxy names"""
        names = []
        for g in self.galaxies:
            names.append(g.get_name())
        return names

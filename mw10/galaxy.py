#!/usr/bin/env python

import star

class Galaxy:
    """Class to handle keeping up with galaxy elements, including random
    initialization of a galaxy"""
    def __init__(self):
        """Initialize a galaxy"""
        self.star = star.Star()
        self.name = 'Milky Way 10'

    def __repr__(self):
        """String representation of the galazy"""
        return 'galaxy ' + self.name + ' contains ' + self.star.__repr__()

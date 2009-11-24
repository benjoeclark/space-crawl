#!/usr/bin/env python

class Star:
    """The star class"""
    def __init__(self, location):
        """Star initialization"""
        self.name = 'Sol 10'
        self.location = location

    def __repr__(self):
        return self.name

    def get_location(self):
        return self.location

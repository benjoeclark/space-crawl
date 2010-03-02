#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
    import game
    game.Game()

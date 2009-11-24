#!/usr/bin/env python

from mw10 import game
from mw10 import display

def main():
    text_display = display.TextDisplay()
    g = game.Game(text_display)

if __name__ == '__main__':
    main()

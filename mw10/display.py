#!/usr/bin/env python

import commands
import galaxy
import body
import os

class TextDisplay:
    """Display for playing MW10 in a console"""
    def __init__(self, debug=False):
        """Initialize a TextDisplay"""
        self.width = 61
        self.height = 23
        self.debug = debug
        self.sprites = []
        self.background = []
        self.prompt = ''
        self.screen = ''

    def set_prompt(self, prompt):
        """Set the user propmt"""
        self.prompt = prompt

    def set_sprites(self, sprites):
        """Set the list of sprites"""
        self.sprites = sprites

    def draw(self):
        """Draw the current view state"""
        # Note that when drawing sprites, the y positions are flipped since
        # indexing of the sprites starts from the top and goes down while
        # a normal y-axis starts from the bottom and goes up
        self.screen = self.fill_screen()
        x, y = self.width/2, self.height/2
        line_number = 0
        for item in self.sprites:
            if isinstance(item, str):
                self.insert_text(item, line_number)
                line_number += 1
            elif isinstance(item, galaxy.Galaxy):
                self.insert_symbol(item.symbol, x+item.position[0],
                        y-item.position[1])
            elif isinstance(item, body.Body):
                self.insert_symbol(item.symbol, x+item.position[0],
                        y-item.position[1])
        self.clear()
        print self.screen

    def insert_text(self, line, line_number):
        """Insert the line at the line number"""
        lines = self.screen.splitlines()
        lines[line_number] = line + lines[line_number][len(line):]
        self.screen = '\n'.join(lines)

    def insert_symbol(self, symbol, x, y):
        """Insert the symbol at the given position"""
        lines = self.screen.splitlines()
        lines[y] = lines[y][:x] + symbol + lines[y][x+1:]
        self.screen = '\n'.join(lines)

    def fill_screen(self, buffer=[]):
        """Fill a screen given a set of lines, used for displaying lines
        of text"""
        output = []
        if len(buffer) < self.height:
            for line in buffer:
                output.append(line + ' '*(self.width-len(line)))
            for line in xrange(self.height-len(buffer)):
                output.append(' '*self.width)
        return '\n'.join(output)

    def get_user_input(self):
        """Wait for the user input, and return an action based on it"""
        command = raw_input(self.prompt)
        return command

    def clear(self):
        """Clear the screen if not in debug mode"""
        if not self.debug:
            os.system('clear')

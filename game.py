#!/usr/bin/env python

import curses
import random

class Body():
    '''Class for handling attributes of an astral body'''
    name = None
    pos = None
    symbol = None

class Planet(Body):
    '''Class for handling a planet'''
    def __init__(self, name, pos=[0, 0]):
        '''Initialize a planet'''
        self.name = name
        self.pos = pos
        self.symbol = ord('0')

class Moon(Body):
    '''Class for handling a moon'''
    def __init__(self, name, pos):
        '''Initialize a moon'''
        self.name = name
        self.pos = pos
        self.symbol = ord('(')

class Ship(Body):
    '''Class for handling a ship'''
    destroyed = False

    def destroy(self):
        '''The ship has been destroyed'''
        self.destroyed = True
        self.symbol = ord('~')

    def isdestroyed(self):
        '''Check the destroyed status of the ship'''
        return self.destroyed

class Drone(Ship):
    '''Class for a drone'''
    def __init__(self, name, pos):
        '''Initialize a drone'''
        self.name = name
        self.pos = pos
        self.symbol = ord('d')

class Galaxy():
    '''Class for handling a group of astral bodies'''
    def __init__(self, planet_count=10, ships=['d']*6):
        '''Initialize the galaxy'''
        self.bodies = []
        for planet_counter in xrange(planet_count):
            planet = Planet(str(planet_counter), self.random_position())
            self.bodies.append(planet)
            for moon_counter in range(self.number_of_moons()):
                moon = Moon(str(planet_counter) + '-' + str(moon_counter),
                            self.random_position(2, planet.pos))
                self.bodies.append(moon)
        for ship_type in ships:
            if ship_type == 'd':
                self.bodies.append(Drone('enemy drone', self.random_position()))

    def random_position(self, extent=30, origin=[0, 0]):
        '''Return a random position in the galaxy'''
        # select a position that does not correspond with another body
        pos = None
        while self.already_filled(pos):
            pos = [origin[0] + random.randint(-extent, extent),
                    origin[1] + random.randint(-extent, extent)]
        return pos

    def already_filled(self, pos):
        '''Detect if this position is filled'''
        if pos is None: return True
        for body in self.bodies:
            if pos[0] == body.pos[0] and pos[1] == body.pos[1]:
                return True
        return False

    def number_of_moons(self):
        '''Return a number of moons for a planet'''
        return random.sample([0, 0, 0, 1, 1, 2], 1)[0]

class Player():
    '''Class to keep track of a player's state'''
    def __init__(self):
        '''Initialize the player'''
        self.pos = [0, 0]
        self.symbol = ord('@')

    def move(self, movement):
        '''Change the player position'''
        self.pos[0] -= movement[0]
        self.pos[1] += movement[1]

    def combat(self, ship):
        '''Combat the given ship'''
        ship.destroy()

class Game():
    '''Game class for playing space crawl'''
    def __init__(self, screen):
        '''Initialization for space crawl'''
        curses.curs_set(0) #Make the cursor invisible
        self.screen = screen
        self.h, self.w = self.screen.getmaxyx()
        self.hud_h = self.h
        self.hud_w = self.w/2
        self.hud = self.screen.subwin(self.hud_h, self.hud_w, 0, 0)
        self.console = self.screen.subwin(self.h,
                                        self.w-self.hud_w,
                                        0, self.hud_w) 
        self.galaxy = Galaxy()
        self.player = Player()
        self.ch = None
        self.logfile = open('log', 'w')
        self.run()

    def run(self):
        '''Run the space crawl game'''
        while self.ch is not ord('q'):
            self.screen.clear()
            self.show_state()
            self.ch = self.screen.getch()
            if self.ch == ord('h'):
                self.player.move([-1, 0])
            elif self.ch == ord('j'):
                self.player.move([0, -1])
            elif self.ch == ord('k'):
                self.player.move([0, 1])
            elif self.ch == ord('l'):
                self.player.move([1, 0])
        self.logfile.close()

    def show_object(self, pos, origin, symbol):
        '''Plot the given object with respec to the origin'''
        x, y = self.hud_w/2 - pos[0] + origin[0], self.hud_h/2 - pos[1] + origin[1]
        #self.logfile.write('pos: ' + str(x) + ' ' + str(y))
        if x < 1:
            x = 1
            symbol = '.'
        elif x > self.hud_w-2:
            x = self.hud_w-2
            symbol = '.'
        if y < 1:
            y = 1
            symbol = '.'
        elif y > self.hud_h-2:
            y = self.hud_h-2
            symbol = '.'
        #self.logfile.write(' ' + str(x) + ' ' + str(y) + '\n')
        self.hud.addch(y, x, symbol)

    def show_state(self):
        '''Show the current game state on the screen'''
        self.hud.border()
        for body in self.galaxy.bodies:
            self.show_object(body.pos, self.player.pos, body.symbol)
        self.hud.addch(self.hud_h/2, self.hud_w/2, self.player.symbol)
        self.detect_collision()

    def detect_collision(self):
        '''Detect if the player is in the same position as an object'''
        for body in self.galaxy.bodies:
            if body.pos[0] == self.player.pos[0] and body.pos[1] == self.player.pos[1]:
                if isinstance(body, Ship):
                    self.player.combat(body)
                    if body.isdestroyed():
                        self.console.addstr(1, 1, 'Destroyed ' + body.name)
                else:
                    self.console.addstr(1, 1, 'Found ' + body.name)
        

def main(screen):
    '''Play the game'''
    game = Game(screen)

if __name__=='__main__':
    curses.wrapper(main)

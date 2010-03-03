"""state

Module to handle various game states"""

import space
import player
import circle
import random

class State(object):
    """State superclass"""
    def __init__(self, screen, universe=None):
        """Generic class initialization"""
        self.screen = screen
        self.universe = universe if universe is not None else space.Universe()
        self.start()

    def start(self):
        """Initialization function to be implemented in the subclass"""
        pass


class GalaxySelector(State):
    def start(self):
        self.screen.clear()
        self.generate_universe()
        self.show_universe()

    def handle_key(self, key):
        self.screen.clear()
        if key == ord('j'):
            self.select_direction([1, 0])
        elif key == ord('k'):
            self.select_direction([-1, 0])
        elif key == ord('h'):
            self.select_direction([0, -1])
        elif key == ord('l'):
            self.select_direction([0, 1])
        else:
            return Flight(self.screen, self.universe)
        self.show_universe()

    def select_direction(self, direction):
        base = self.galaxies[self.selection]
        new_base = None
        position = base[:]
        if [base[0]+direction[0], base[1]+direction[1]] in self.paths:
            while new_base is None:
                position[0] += direction[0]
                position[1] += direction[1]
                if position in self.galaxies:
                    self.selection = self.galaxies.index(position)
                if position not in self.paths:
                    return None

    def generate_universe(self):
        height, width = self.screen.getmaxyx()
        self.screen.addstr(0, 0, 'Select a galaxy')
        self.positions = []
        for xcount in range(1, height):
            for ycount in range(width):
                self.positions.append([xcount, ycount])
        self.galaxies = []
        self.galaxies.append(self.pull_position([10, 39]))
        self.galaxies.append(self.pull_position([13, 39]))
        self.paths = []
        self.paths.append(self.pull_position([11, 39]))
        self.paths.append(self.pull_position([12, 39]))
        for galaxy_count in range(30):
            base_galaxy = random.choice(self.galaxies)
            position = self.get_possible_position(base_galaxy)
            if position is not None:
                self.galaxies.append(self.pull_position(position))
                self.get_paths(base_galaxy, self.galaxies[-1])
        self.selection = 0

    def show_selection(self):
        self.screen.addstr(self.galaxies[self.selection][0], self.galaxies[self.selection][1], '^')

    def get_paths(self, base, remote):
        for x in range(base[0]+1, remote[0]):
            if [x, base[1]] in self.positions:
                self.paths.append(self.pull_position([x, base[1]]))
        for x in range(remote[0]+1, base[0]):
            if [x, base[1]] in self.positions:
                self.paths.append(self.pull_position([x, base[1]]))
        for y in range(base[1]+1, remote[1]):
            if [base[0], y] in self.positions:
                self.paths.append(self.pull_position([base[0], y]))
        for y in range(remote[1]+1, base[1]):
            if [base[0], y] in self.positions:
                self.paths.append(self.pull_position([base[0], y]))

    def pull_position(self, position):
        return self.positions.pop(self.positions.index(position))

    def get_possible_position(self, base):
        possible = []
        up = True
        up = ([base[0]-1, base[1]] not in self.paths) and \
            ([base[0]-1, base[1]] not in self.galaxies)
        for x in range(base[0]-2, 0, -1):
            if up:
                if [x, base[1]] in self.positions:
                    possible.append([x, base[1]])
                else:
                    up = False
        down = True
        down = ([base[0]+1, base[1]] not in self.paths) and \
            ([base[0]+1, base[1]] not in self.galaxies)
        for x in range(base[0]+2, 24):
            if down:
                if [x, base[1]] in self.positions:
                    possible.append([x, base[1]])
                else:
                    down = False
        left = True
        left = ([base[0], base[1]-1] not in self.paths) and \
            ([base[0], base[1]-1] not in self.galaxies)
        for y in range(base[1]-2, -1, -1):
            if left:
                if [base[0], y] in self.positions:
                    possible.append([base[0], y])
                else:
                    left = False
        right = True
        right = ([base[0], base[1]+1] not in self.paths) and \
            ([base[0], base[1]+1] not in self.galaxies)
        for y in range(base[1]+2, 80):
            if right:
                if [base[0], y] in self.positions:
                    possible.append([base[0], y])
                else:
                    right = False
        if len(possible) == 0:
            return None
        return random.choice(possible)

    def show_universe(self):
        for path in self.paths:
            self.screen.addstr(path[0], path[1], '.')
        for galaxy, index in zip(self.galaxies, range(len(self.galaxies))):
            self.screen.addstr(galaxy[0], galaxy[1], 'O')
        self.show_selection()



class New(State):
    def start(self):
        """Welcome the user and start a new game"""
        self.screen.clear()
        self.screen.addstr(0, 0, 'Welcome to MW10')
        self.screen.addstr(1, 0, 'press any key to launch into the unknown')

    def handle_key(self, key):
        """On any keypress, launch the ship"""
        self.screen.clear()
        return Flight(self.screen, self.universe)


class Flight(State):
    def start(self):
        self.show_galaxy()

    def handle_key(self, key):
        if key == ord('k'):
            self.universe.player.move(-1, 0)
        elif key == ord('j'):
            self.universe.player.move(1, 0)
        elif key == ord('h'):
            self.universe.player.move(0, -1)
        elif key == ord('l'):
            self.universe.player.move(0, 1)
        elif key == ord('i'):
            return Inventory(self.screen, self.universe)
        self.screen.clear()
        self.show_galaxy()
        collision = self.universe.detect_collision()
        if len(collision) > 0:
            combat_collision = False
            orbit_collision = False
            for body in collision:
                if isinstance(body, space.Planet):
                    orbit_collision = True
                elif isinstance(body, player.Npc):
                    combat_collision = True
            if combat_collision:
                return Combat(self.screen, self.universe, collision)
            elif orbit_collision:
                return Orbit(self.screen, self.universe, collision)

    def show_galaxy(self):
        height, width = self.screen.getmaxyx()
        self.screen.addstr(height/2, width/2, self.universe.player.symbol)
        for body in self.universe.galaxy.bodies:
            x, y = self.relative_position(body, self.universe.player)
            x += height/2
            y += width/2
            if x < 1:
                x = 1
            elif x >= height-2:
                x = height-2
            if y < 1:
                y = 1
            elif y >= width-2:
                y = width-2
            self.screen.addstr(x, y, body.symbol)

    def relative_position(self, body, player):
        return body.x - player.x, body.y - player.y


class Inventory(State):
    def start(self):
        self.screen.clear()
        self.show_ship()
        self.show_inventory()

    def handle_key(self, key):
        self.screen.clear()
        return Flight(self.screen, self.universe)

    def show_ship(self):
        ship_image = self.universe.player.ship.get_image()
        ship_status = ''
        ship_status += str(self.universe.player.ship.get_hull()) 
        ship_status += ' hull | '
        ship_status += str(self.universe.player.ship.get_shield())
        ship_status += ' shield'
        self.screen.addstr(0, 0, ship_status)
        for line, line_number in zip(ship_image, range(len(ship_image))):
            self.screen.addstr(1+line_number, 0, line)

    def show_inventory(self):
        pass



class CollisionState(State):
    def __init__(self, screen, universe, collisions):
        self.collisions = collisions
        super(CollisionState, self).__init__(screen, universe)


class Combat(CollisionState):
    def start(self):
        self.combatants = []
        for body in self.collisions:
            if isinstance(body, player.Npc):
                self.combatants.append(body)
        self.screen.clear()
        self.screen.addstr(0, 0, 'In combat with ' + self.combatants[0].name)

    def handle_key(self, key):
        self.screen.clear()
        return Flight(self.screen, self.universe)


class Orbit(CollisionState):
    def start(self):
        self.planet = self.collisions[0]
        self.orbit = circle.Path(self.planet.radius+2, path_symbol='.')
        self.screen.clear()
        self.screen.addstr(0, 0, 'Orbiting ' + self.planet.name)
        self.show_planet()

    def handle_key(self, key):
        self.screen.clear()
        if key == ord(' '):
            self.orbit.next()
            self.show_planet()
        else:
            return Flight(self.screen, self.universe)

    def show_planet(self):
        for line, line_number in zip(self.orbit.get_circle_strings(),
                range(len(self.orbit.get_circle_strings()))):
            self.screen.addstr(1+line_number, 0, line)
        for line, line_number in zip(self.planet.image, range(len(self.planet.image))):
            spaces_count = len(line) - len(line.lstrip())
            self.screen.addstr(3+line_number, 4+spaces_count, line.strip())


class Docked(CollisionState):
    def start(self):
        self.station = self.collisions[0]
        self.screen.clear()
        self.screen.addstr(0, 0, 'Docked at ' + self.station.name)

    def handle_key(self, key):
        self.screen.clear()
        return Flight(self.screen, self.universe)

"""ship.py

Module for handling the ships in the game
key for ship images:
-\/|    hull
!       weapon bay
0       cargo bay
*       power supply
^       thruster
"""

import parts

class Ship(object):
    """Main ship superobject"""
    def __init__(self):
        self.weapons = []
        self.cargo = []
        self.power = []
        self.thrusters = []
        self.set_image()
        self.set_default_parts()
        self.construct()

    def set_image(self):
        self.image = []

    def set_default_parts(self):
        self.default_weapon = parts.MiningLazer()
        self.default_power = parts.BasicPower()
        self.default_thruster = parts.MachThruster()

    def construct(self):
        self.hull = 100.
        self.shield = 10.
        for count in range(self.get_weapon_bays()):
            self.weapons.append(self.default_weapon)
        for count in range(self.get_power_supplies()):
            self.power.append(self.default_power)
        for count in range(self.get_thrusters()):
            self.thrusters.append(self.default_thruster)

    def get_image(self):
        return self.image

    def get_weapon_bays(self):
        """Get the number of weapon bays on the ship"""
        return self.symbol_search('!')

    def get_cargo_bays(self):
        """Get the number of cargo bays on the ship"""
        return self.symbol_search('0')

    def get_power_supplies(self):
        """Get the number of power supplies on the ship"""
        return self.symbol_search('*')

    def get_thrusters(self):
        """Get the number of thrusters on the ship"""
        return self.symbol_search('^')

    def symbol_search(self, symbol):
        """Return the number of instances of the symbol"""
        count = 0
        for line in self.image:
            count += line.count(symbol)
        return count

    def get_damage_output(self):
        damage = 0.
        for weapon in self.weapons:
            damage += weapon.max_output
        return damage

    def get_shield(self):
        return self.shield

    def get_hull(self):
        return self.hull


class Pod(Ship):
    def set_image(self):
        self.image = [
            r'  -  ',
            r' / \ ',
            r'!|0|!',
            r' \*/ ',
            r'  ^  ']

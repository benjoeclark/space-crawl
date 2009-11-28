class Ship:
    """The ship class
    Key for the ship's image:
    -, /, \, | = hull
    ! = weapon bay
    0 = cargo bay
    * = power supply
    ^ = thruster"""
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


class Pod(Ship):
    """The pod ship"""
    def __init__(self):
        """Initialize the pod ship"""
        self.image = [
                r'  -  ',
                r' /0\ ',
                r'!|*|!',
                r' \^/ ',
                r'  -  ']

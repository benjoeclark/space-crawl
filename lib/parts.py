class Weapon(object):
    pass


class EnergyWeapon(Weapon):
    pass


class MiningLazer(EnergyWeapon):
    def __init__(self):
        self.max_output = 1.


class Power(object):
    pass


class BasicPower(Power):
    def __init__(self):
        self.max_output = 10.


class Thruster(object):
    pass


class MachThruster(Thruster):
    def __init__(self):
        self.max_output = 1.

class Planet:
    """Planet class"""
    def __init__(self, position, name, symbol='0'):
        """Initialize the planet"""
        self.position = position
        self.name = name
        self.symbol = symbol
        self.contents = []

    def append(self, item):
        """Append the item to the planet's contents"""
        self.contents.append(item)

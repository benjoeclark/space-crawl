import math

class Circle(object):
    def __init__(self, radius, symbol=' ', font_ratio=0.45):
        self.radius = radius
        self.font_ratio = font_ratio
        self.symbol = symbol
        # generate angles around circle
        angles = []
        for degree in range(360):
            angles.append(math.pi*degree/180.)
        # generate positions
        positions = []
        for angle in angles:
            positions.append([radius*math.sin(angle), radius*math.cos(angle)/font_ratio])
        # round to integer values
        blocks = [[int(round(p[0])), int(round(p[1]))] for p in positions]
        # remove duplicate copies
        self.pixels = []
        for block in blocks:
            if block not in self.pixels:
                self.pixels.append(block)
        self.extent = int(round(radius))*2
        self.horiz_extent = int(round(radius/font_ratio))*2
        self.screen = [' '*(self.horiz_extent+1)]*(self.extent+1)
        for pixel in self.pixels:
            self.place_symbol(pixel, self.symbol)

    def get_circle_strings(self):
        return self.screen

    def place_symbol(self, pixel, symbol):
        x = pixel[0]+self.extent/2
        y = pixel[1]+self.horiz_extent/2
        self.screen[x] = self.screen[x][:y] + symbol + self.screen[x][y+1:]


class Path(Circle):
    def __init__(self, radius, object_symbol='@', path_symbol=' ', font_ratio=0.45):
        self.object_symbol = object_symbol
        super(Path, self).__init__(radius, path_symbol, font_ratio)
        self.current_pixel = 0
        self.place_symbol(self.pixels[self.current_pixel], self.object_symbol)

    def next(self):
        self.place_symbol(self.pixels[self.current_pixel], self.symbol)
        self.current_pixel += 1
        if self.current_pixel == len(self.pixels):
            self.current_pixel = 0
        self.place_symbol(self.pixels[self.current_pixel], self.object_symbol)
        

if __name__ == '__main__':
    circle = Circle(8, '0')
    print '\n'.join(circle.get_circle_strings())
    path = Path(3, path_symbol='.')
    print '\n'.join(path.get_circle_strings())
    path.next()
    print '\n'.join(path.get_circle_strings())
    path.next()
    print '\n'.join(path.get_circle_strings())

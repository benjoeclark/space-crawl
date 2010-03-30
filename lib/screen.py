class Screen:
    def __init__(self, height=23, width=79):
        self.height = height
        self.width = width
        self.view = None
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = '1234567'
        self.clear()

    def clear(self):
        self.view = [' ' * self.width] * self.height

    def addstr(self, x, y, s):
        self.view[x] = self.view[x][:y] + s + self.view[x][y+len(s):]

    def border(self):
        self.view[0] = '-' * self.width
        self.view[-1] = '-' * self.width
        for line in xrange(1, self.height-1):
            self.view[line] = '|' + self.view[line][1:-1] + '|'

    def ruler(self):
        for index in range(len(self.letters)):
            self.view[0] = self.view[0][:2+3*index] + self.letters[index] + \
                            self.view[0][3+3*index:]
        for index in range(len(self.numbers)):
            self.view[2+3*index] = self.numbers[index] + self.view[2+3*index][1:]

    def grid(self):
        for row in xrange(7):
            self.view[2+3*row] = self.view[2+3*row][0] + '.'*(self.width-1)
        for column in xrange(26):
            for row in xrange(1, self.height-1):
                self.view[row] = self.view[row][:2+3*column] + '.' + \
                            self.view[row][3+3*column:]

    def grid_add(self, position, symbol):
        self.addstr(2+3*position[0], 2+3*position[1], symbol)

    def plot_from_center(self, position, symbol):
        x = position[0] + self.height/2
        y = position[1] + self.width/2
        self.addstr(x, y, symbol)

    def prompt(self):
        self.view[-1] = '>>>'

    def draw(self):
        print '\n' * 100
        print '\n'.join(self.view)

if __name__ == '__main__':
    import random
    screen = Screen()
    screen.ruler()
    screen.grid()
    screen.prompt()
    for star in xrange(10):
        x = random.randint(1, screen.height-2)
        y = random.randint(1, screen.width-1)
        screen.addstr(x, y, '0')
    screen.draw()

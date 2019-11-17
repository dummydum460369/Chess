from Vectors2d import *


class Box(object):
    def __init__(self, color, piece=None):
        self.color = color
        self.piece = piece

    def swap_color(self):
        self.color = 'W' if self.color == 'B' else 'B'

    def __str__(self):
        return f'{self.piece} on {self.color}'

    def __repr__(self):
        # return f'{self.piece} on {self.color}'
        return self.color


class Board(object):
    def __init__(self):
        self.places = {(x, y): Box('B' if (x % 2 == 0) else 'W') for y in range(8) for x in range(8)}
        for i in self.places:
            if i[1] % 2 != 0:
                self.places[i].swap_color()


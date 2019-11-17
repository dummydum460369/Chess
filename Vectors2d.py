from Static_Methods import *


class Vector2d:
    def __init__(self, x=0.0 + 0j, y=0.0 + 0j):
        self.x = x
        self.y = y
        Vector2d.system = '2 Dimensional'

    @property
    def val(self):
        return {'X': self.x, 'Y': self.y}

    @val.setter
    def val(self, obj):
        if isinstance(obj, dict):
            for i in obj:
                if i in 'iIxXîÎ':
                    self.x = obj[i]
                elif i in 'jJyYĵĴ':
                    self.y = obj[i]
            self.x = obj['X']
            self.y = obj['Y']
        result = []
        if isinstance(obj, Vc.Vector2d):
            result = [obj.val['X'], obj.val['Y']]
        elif isinstance(obj, tuple) or isinstance(obj, list):
            if len(obj) == 2:
                for i in obj:
                    if isinstance(i, int) or isinstance(i, float) or isinstance(i, complex):
                        result.append(i)
                    elif i.isinstance(str):
                        temp_obj, component = str_changer(i)
                        if component is None:
                            result.append(temp_obj)
                        elif component == 'x':
                            result = [temp_obj] + result
                        elif component == 'y':
                            result = result + [temp_obj]
        elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
            result = [obj, obj]
        elif isinstance(obj, str):
            temp_obj, component = str_changer(obj)
            if component == 'xy':
                result = temp_obj.copy()
        self.x = result[0]
        self.y = result[1]

    @property
    def math_form(self):
        # Returns Rectangular Coordinates in vector format
        return f"{self.val['X']}î+{self.val['Y']}ĵ"

    @math_form.setter
    def math_form(self, obj):
        result = []
        if isinstance(obj, Vc.Vector2d):
            result = [obj.val['X'], obj.val['Y']]
        elif isinstance(obj, tuple) or isinstance(obj, list):
            if len(obj) == 2:
                for i in obj:
                    if isinstance(i, int) or isinstance(i, float) or isinstance(i, complex):
                        result.append(i)
                    elif i.isinstance(str):
                        temp_obj, component = str_changer(i)
                        if component is None:
                            result.append(temp_obj)
                        elif component == 'x':
                            result = [temp_obj] + result
                        elif component == 'y':
                            result = result + [temp_obj]
        elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
            result = [obj, obj]
        elif isinstance(obj, str):
            temp_obj, component = str_changer(obj)
            if component == 'xy':
                result = temp_obj.copy()
        self.x = result[0]
        self.y = result[1]

    def increment(self, x=0, y=0):
        # Increments given x and/or y value to instance
        # Warning! Doesn't return anything
        self.val['X'], self.val['Y'] = self.val['X'] + x, self.val['Y'] + y
        self.val = {'X': self.val['X'], 'Y': self.val['Y']}

    @operand_optimize
    def __add__(self, obj):
        return Vector2d(x=(self.val['X'] + obj[0]), y=(self.val['Y'] + obj[1]))

    @operand_optimize
    def __sub__(self, obj):
        return Vector2d(x=(self.val['X'] - obj[0]), y=(self.val['Y'] - obj[1]))

    @operand_optimize
    def __mul__(self, obj):
        return (self.x * obj[0]) + (self.y * obj[1])

    @property
    def magnitude(self):
        return ((self.x * self.x) + (self.y * self.y)) ** 0.5

    @operand_optimize
    def __eq__(self, other):
        if self.x == other[0] and self.y == other[1]:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vector2d):
            if self.magnitude < other.magnitude:
                return True
        return False

    def __le__(self,other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self,other):
        return not self.__le__(other)

    def __ge__(self,other):
        return self.__eq__(other) or self.__gt__(other)

class vector2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def plus(self, other):
        return vector2D(self._x + other._x, self._y + other._y)


a = vector2D(2,2)
b = vector2D(-1,2)
c = a.plus(b)
class Shape:
    """Abstract shape class"""

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def is_point_included(self, x, y):
        raise NotImplementedError()


class Point(Shape):
    """Point shape"""

    def __init__(self, x, y):
        super().__init__(x, y)

    def is_point_included(self, x, y):
        return x == self.position_x and y == self.position_y


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def is_point_included(self, x, y):
        return x >= self.position_x and x < self.position_x + self.width and \
               y >= self.position_y and y < self.position_y + self.height


class Square(Rectangle):
    """Square shape"""

    def __init__(self, x, y, length):
        super().__init__(x, y, length, length)

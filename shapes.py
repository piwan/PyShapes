class Shape:
    """Abstract shape class"""

    def __init__(self, x, y, color='X'):
        self.position_x = x
        self.position_y = y
        self.color = color

    def is_point_included(self, x, y):
        raise NotImplementedError()


class Point(Shape):
    """Point shape"""

    def __init__(self, x, y, color='X'):
        super().__init__(x, y, color)

    def is_point_included(self, x, y):
        return x == self.position_x and y == self.position_y


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, x, y, width, height, color='X'):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def is_point_included(self, x, y):
        return x >= self.position_x and x < self.position_x + self.width and \
               y >= self.position_y and y < self.position_y + self.height


class Square(Rectangle):
    """Square shape"""

    def __init__(self, x, y, length, color='X'):
        super().__init__(x, y, length, length, color)

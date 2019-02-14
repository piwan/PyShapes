class Shape:
    """Abstract shape class"""

    def __init__(self, x, y, color='X', is_filled=False):
        self.position_x = x
        self.position_y = y
        self.color = color
        self.is_filled = is_filled

    def is_point_included(self, x, y):
        raise NotImplementedError()

    def move(self, by_x, by_y):
        self.position_x += by_x
        self.position_y += by_y


class Point(Shape):
    """Point shape"""

    def __init__(self, x, y, color='X', is_filled=False):
        super().__init__(x, y, color, is_filled)

    def is_point_included(self, x, y):
        return x == self.position_x and y == self.position_y


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, x, y, width, height, color='X', is_filled=False):
        super().__init__(x, y, color, is_filled)
        self.width = width
        self.height = height

    def is_point_included(self, x, y):
        if self.is_filled:
            return x >= self.position_x and x < self.position_x + self.width and \
                   y >= self.position_y and y < self.position_y + self.height
        else:
            return y == self.position_y and x >= self.position_x and x < self.position_x + self.width or \
                   y == self.position_y + self.height - 1 and x >= self.position_x and x < self.position_x + self.width or \
                   x == self.position_x and y >= self.position_y and y < self.position_y + self.height or \
                   x == self.position_x + self.width - 1 and y >= self.position_y and y < self.position_y + self.height


class Square(Rectangle):
    """Square shape"""

    def __init__(self, x, y, length, color='X', is_filled=False):
        super().__init__(x, y, length, length, color, is_filled)


class Circle(Shape):
    """Circle shape"""

    def __init__(self, x, y, radius, color='X', is_filled=False):
        super().__init__(x, y, color, is_filled)
        self.radius = radius

    def is_point_included(self, x, y):
        circle_function = (x - self.position_x) ** 2 + (y - self.position_y) ** 2 - self.radius ** 2.0
        if self.is_filled:
            return circle_function <= 1.0
        else:
            return abs(circle_function) <= self.radius

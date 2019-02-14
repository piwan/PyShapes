class ConsoleDrawingPane:

    def __init__(self, width=100, height=20):
        self.width = width
        self.height = height
        self.shapes = []

    def draw(self):
        # The algorithm:
        # we iterate point by point (pixel by pixel)
        # for each point we check if there is any Shape that contains it
        for y in range(0, self.height - 1):
            for x in range(0, self.width - 1):
                drawing_symbol = 'X'
                empty_symbol = ' '
                symbol = empty_symbol

                for shape in self.shapes:
                    if shape.is_point_included(x, y):
                        symbol = drawing_symbol

                print(symbol, end='')

            print()  # enter new line

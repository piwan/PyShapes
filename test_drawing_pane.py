from drawing_pane import ConsoleDrawingPane
from shapes import Rectangle, Point, Square

pane = ConsoleDrawingPane()
pane.shapes = [
    Rectangle(1, 1, 3, 5, 'R'),
    Point(29, 9),
    Point(0, 0, 'G'),
    Square(10, 0, 10, 'Y')
]
pane.draw()

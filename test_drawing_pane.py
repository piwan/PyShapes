from drawing_pane import ConsoleDrawingPane
from shapes import Rectangle, Point

pane = ConsoleDrawingPane()
pane.shapes = [
    Rectangle(1, 1, 3, 5),
    Point(29, 9),
    Point(0, 0)
]
pane.draw()

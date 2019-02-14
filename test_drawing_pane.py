from drawing_pane import ConsoleDrawingPane
from shapes import Rectangle, Point, Square, Circle

pane = ConsoleDrawingPane()
pane.shapes = [
    Rectangle(1, 1, 3, 5, 'R'),
    Point(29, 9),
    Point(0, 0, 'G'),
    Square(10, 0, 10, 'Y'),
    Circle(20, 10, 5)
]

print("Before changes:")
pane.draw()

pane.shapes[0].move(1, 10)
pane.shapes[1].move(1, 1)
pane.shapes[3].is_filled = True
pane.shapes[4].color = 'R'
print("After changes:")
print(pane)

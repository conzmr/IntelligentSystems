import turtle

walls = [(0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
     (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1)]

path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
(1, 4), (2, 4), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)]

background_color = "black"

obstacles_color = "white"

path_color = "red"

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

    def set_color(self, color):
        self.color(color)

def paint(list, pen, color):
    pen.set_color(color)
    for x in range (len(list)):
        screen_x = -288 + (list[x][0] * 24)
        screen_y = 288 - (list[x][1] * 24)
        pen.goto(screen_x, screen_y)
        pen.stamp()

def setup_maze():
    wn = turtle.Screen()
    wn.title("A* Maze")
    wn.bgcolor(background_color)
    wn.setup(700,700)
    pen = Pen()
    paint(walls, pen, obstacles_color )
    paint(path, pen, path_color)

setup_maze()

while True:
    pass

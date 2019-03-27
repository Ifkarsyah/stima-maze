import turtle
import time
from algo import maze


class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.x, self.y = x, y
        self.speed(0)


class Trail(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(0.2, 0.2)
        self.color("blue")
        self.penup()
        self.x, self.y = x, y
        self.speed(0)


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Stima Maze")
wn.setup(700, 700)


def draw_maze(maze):
    block = Block()
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            sc_x, sc_y = -288 + (x*24), 288 - (y*24)
            if maze[y][x] == "1":
                block.goto(sc_x, sc_y)
                block.stamp()


player = Player(0, 1)
draw_maze(maze)


while True:
    pass

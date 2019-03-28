import turtle
import astar
from utils import maze


class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self, point):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.x, self.y = point
        self.speed(0)


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Stima Maze")
wn.setup(1000, 1000)


def pos_to_sc(x, y):
    return (-432 + (x * 12), 312 - (y * 12))


def draw_maze(maze, pathway):
    b = Block()
    p = Player(pathway[0])
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                b.goto(pos_to_sc(x, y))
                b.stamp()
    for path in pathway:
        x, y = path
        p.goto(pos_to_sc(x, y))
        p.stamp()


# SAMPLE SOLUTION = LIST OF POS WHERE PLAYER TRAVEL
path_astar = [(y, x) for (x, y) in astar.jalurAStar]
draw_maze(maze, path_astar)


while True:
    pass

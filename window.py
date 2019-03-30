from turtle import Turtle, Screen
from astar import jalurAStar
from bfs import bfs
from utils import maze, rows, cols, start, finish
import time

class Block(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)

class BlackBlock(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.shapesize(0.5)
        self.penup()
        self.speed(0)

class Player(Turtle):
    def __init__(self, point):
        Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.x, self.y = point
        self.speed(0)

class Start(Turtle):
    def __init__(self, point):
        Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.shapesize(0.5)
        self.penup()
        self.x, self.y = point
        self.speed(0)

class Finish(Turtle):
    def __init__(self, point):
        Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.shapesize(0.5)
        self.penup()
        self.x, self.y = point
        self.speed(0)

wn = Screen()
wn.bgcolor("black"), wn.title("Stima Maze"), wn.setup(1000, 1000)

def pos_to_sc(x, y):
    return (-432 + (x * 12), 312 - (y * 12))

def draw_maze(maze):
    b = Block()
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                b.goto(pos_to_sc(x, y))
                b.stamp()

def draw_path(pathway):
    #Draw Start and Finish
    s = Start(pathway[0])
    x, y = pathway[0];
    s.goto(pos_to_sc(x, y))
    s.stamp()

    f = Finish(pathway[len(pathway)-1])
    x, y = pathway[len(pathway)-1];
    f.goto(pos_to_sc(x, y))
    f.stamp()

    #Draw player movement
    p = Player(pathway[0])
    for path in pathway:
        if((path != pathway[0]) and (path != pathway[len(pathway)-1])):
            x, y = path
            p.goto(pos_to_sc(x, y))
            p.stamp()

def reset_path(pathway):
    #Reset player movement
    p = BlackBlock()
    for path in pathway:
        if((path != pathway[0]) and (path != pathway[len(pathway)-1])):
            x, y = path
            p.goto(pos_to_sc(x, y))
            p.stamp()

path_astar = [(y, x) for (x, y) in jalurAStar]
path_bfs = [(y, x) for (x, y) in bfs(start, finish)]
print("THIS IS BFS PATH\n")
draw_maze(maze)
draw_path(path_bfs)
time.sleep(5)
reset_path(path_bfs)

print("THIS IS A* PATH")
draw_path(path_astar)

wn.exitonclick()

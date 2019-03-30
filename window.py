from turtle import Turtle, Screen
from astar import jalurAStar
from bfs import bfs
from utils import maze, rows, cols, start, finish
import time

#Block class, for walls
class Block(Turtle):
    def __init__(self,color1):
        Turtle.__init__(self)
        self.shape("square")
        self.color(color1)
        self.shapesize(0.5)
        self.penup()
        self.speed(0)

#Route class, for drawing route
class Route(Turtle):
    def __init__(self, point):
        Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.x, self.y = point
        self.speed(0)

wn = Screen()
wn.bgcolor("black"), wn.title("Stima Maze"), wn.setup(1000, 1000)

def pos_to_sc(x, y):
    return (-432 + (x * 12), 312 - (y * 12))

def draw_maze(maze):
    b = Block("white")
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                b.goto(pos_to_sc(x, y))
                b.stamp()

def draw_path(pathway):
    #Draw Start and Finish
    s = Block("red")
    x, y = pathway[0];
    s.goto(pos_to_sc(x, y))
    s.stamp()

    f = Block("green")
    x, y = pathway[len(pathway)-1];
    f.goto(pos_to_sc(x, y))
    f.stamp()

    #Draw the route
    p = Route(pathway[0])

    for i in range(1 , len(pathway)-1):
        x, y = pathway[i]
        p.goto(pos_to_sc(x, y))
        p.stamp()

def reset_path(pathway):
    #Reset route drawn
    p = Block("black")
    for path in pathway:
        if((path != pathway[0]) and (path != pathway[len(pathway)-1])):
            x, y = path
            p.goto(pos_to_sc(x, y))
            p.stamp()

path_astar = [(y, x) for (x, y) in jalurAStar]
path_bfs = [(y, x) for (x, y) in bfs(start, finish)]
print("This is BFS path\n")
draw_maze(maze)
draw_path(path_bfs)

answer = wn.textinput("This is BFS path", "Press 'OK' to see A* path?")

reset_path(path_bfs)
draw_path(path_astar)

wn.exitonclick()

import turtle
import time
from algo import maze, Point, pos_start, pos_finish, path
# MODELS


class Block(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self, point_init):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.pos = point_init
        self.speed(0)


class Trail(turtle.Turtle):
    def __init__(self, point_init):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(0.2, 0.2)
        self.color("blue")
        self.penup()
        self.pos = point_init
        self.speed(0)


# WINDOWS
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Stima Maze")
wn.setup(700, 700)


# DRAW
def draw_maze(maze):
    global block
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char_code = maze[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            if char_code == "1":
                block.goto(screen_x, screen_y)
                block.stamp()


def draw_player(p):
    screen_x = -288 + (p.pos.x*24)
    screen_y = 288 - (p.pos.y*24)
    p.goto(screen_x, screen_y)


def draw_path(path, p):
    for pos in path:
        t = Trail(p.pos)
        screen_x = -288 + (pos.x*24)
        screen_y = 288 - (pos.y*24)
        p.goto(screen_x, screen_y)
        t.goto(screen_x, screen_y)
        t.stamp()
        time.sleep(0.5)


block = Block()
player = Player(pos_start)

# draw
draw_maze(maze)
draw_player(player)
draw_path(path, player)

while True:
    pass

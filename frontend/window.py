import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Stima Maze")
wn.setup(700, 700)


class Point():
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


class Pen(turtle.Turtle):
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
        self.speed(0)
        self.pos = point_init


# DATA
maze = ["11111111111",
        "00001000001",
        "11101011101",
        "10001010001",
        "10111010111",
        "10100010001",
        "10101010101",
        "10101010101",
        "10101010101",
        "10001010100",
        "11111111111"]
pos_start = Point(0, 1)
pos_finish = Point(10, 9)
path = [Point(0, 1),
        Point(1, 1),
        Point(2, 1),
        Point(3, 1),
        Point(3, 2),
        Point(3, 3)]


def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char_code = maze[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            if char_code == "1":
                pen.goto(screen_x, screen_y)
                pen.stamp()


def draw_player(p):
    screen_x = -288 + (p.pos.x*24)
    screen_y = 288 - (p.pos.y*24)
    p.goto(screen_x, screen_y)


def draw_path(path, p):
    for pos in path:
        screen_x = -288 + (pos.x*24)
        screen_y = 288 - (pos.y*24)
        p.goto(screen_x, screen_y)
        time.sleep(1)


pen = Pen()
player = Player(pos_start)


draw_maze(maze)
draw_player(player)
draw_path(path, player)

while True:
    pass

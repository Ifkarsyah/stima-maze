import queue


class Point():
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# MAZE ['1111111111111','100000000000',.....,'000000111']
maze = open('maze.txt', 'r').read().splitlines()


def search_door():
    # UTIL: FINDING DOOR
    doors = []
    for y in range(len(maze)):
        if maze[y][0] == '0':
            doors.append(Point(0, y))
        if maze[y][len(maze[y])-1] == '0':
            doors.append(Point(len(maze[y])-1, y))
    for x in range(len(maze[0])):
        if maze[0][x] == '0':
            doors.append(Point(x, 0))
        if maze[len(maze)-1][x] == '0':
            doors.append(Point(len(maze)-1, 0))
    return (doors[0], doors[1])


pos_start, pos_finish = search_door()
path = [pos_start, Point(1, 1), Point(2, 1), Point(3, 1), pos_finish]

maze = open('maze.txt', 'r').read().splitlines()


def search_door(maze):
    rows = len(maze)
    cols = len(maze[0])
    doors = [(x, 0) for x in range(rows) if maze[0][x] == '0']
    doors += [(x, cols-1) for x in range(rows) if maze[cols-1][x] == '0']
    doors += [(0, y) for y in range(cols) if maze[y][0] == '0']
    doors += [(rows-1, y) for y in range(cols) if maze[y][rows-1] == '0']
    return set(doors)


start, finish = search_door(maze)
# Sample Result: start = (0,11); finish = (40,27)

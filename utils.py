from pprint import pprint


def readMatrix(namaFile):
    maze = []
    file = open(namaFile, "r")
    for line in file:
        listOfInt = list(line)
        listOfInt.pop(len(listOfInt) - 1)
        for i in range(len(listOfInt)):
            listOfInt[i] = int(listOfInt[i])
        maze.append(listOfInt)
    file.close()
    return maze


maze = readMatrix('maze_extra.txt')


def search_door(maze):
    rows = len(maze)
    cols = len(maze[0])
    doors = [(0, c) for c in range(cols) if maze[0][c] == 0]
    doors += [(rows - 1, c) for c in range(cols) if maze[rows - 1][c] == 0]
    doors += [(r, 0) for r in range(rows) if maze[r][0] == 0]
    doors += [(r, cols - 1) for r in range(rows) if maze[r][cols - 1] == 0]
    return sorted(set(doors))


start, finish = search_door(maze)
print(start, finish)

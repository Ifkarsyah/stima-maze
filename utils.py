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


maze = readMatrix('maze_small.txt')
rows, cols = len(maze), len(maze[0])


def search_door():
    doors = [(0, c) for c in range(cols) if maze[0][c] == 0]
    doors += [(rows - 1, c) for c in range(cols) if maze[rows - 1][c] == 0]
    doors += [(r, 0) for r in range(rows) if maze[r][0] == 0]
    doors += [(r, cols - 1) for r in range(rows) if maze[r][cols - 1] == 0]
    return sorted(set(doors))


start, finish = search_door(maze)


def pos_add(a, b):  # pos_add((1,1),(1,2)) --> (2,3)
    return tuple(map(sum, zip(a, b)))


def in_range(node):  # check if (r,c) still in maze --> bool
    r, c = node
    return c >= 0 and c < cols and r >= 0 and r < rows


def neighbors(node):  # neighbors((1,0)) --> [(1, 1), (2, 0), (0, 0)]
    ways = [pos_add(node, w) for w in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    return list(filter(in_range, ways))

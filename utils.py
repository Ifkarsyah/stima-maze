from sys import argv


def pos_add(a, b):  # pos_add((1,1),(1,2)) --> (2,3)
    return tuple(map(sum, zip(a, b)))


def in_range(node):  # check if (r,c) still in maze --> bool
    r, c = node
    return c >= 0 and c < cols and r >= 0 and r < rows


def neighbors(node):  # neighbors((1,0)) --> [(1, 1), (2, 0), (0, 0)]
    ways = [pos_add(node, w) for w in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    return list(filter(in_range, ways))


def read_matrix(filename):  # --> matrix of int --> [[1,...],[0,1,...],...]
    with open(filename, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
        maze = [[int(c) for c in maze[r]] for r in range(len(maze))]
    return maze


maze = read_matrix(argv[1])
rows, cols = len(maze), len(maze[0])


# def search_door():  # hole in the border of maze --> (1,0), (9,10)
#    doors = [(0, c) for c in range(cols) if maze[0][c] == 0]
#    doors += [(rows - 1, c) for c in range(cols) if maze[rows - 1][c] == 0]
#    doors += [(r, 0) for r in range(rows) if maze[r][0] == 0]
#    doors += [(r, cols - 1) for r in range(rows) if maze[r][cols - 1] == 0]
#    return sorted(set(doors))


# start, finish = search_door()  # hole in the border of maze --> (1,0), (9,10)
def valid(start):  # or finish
    x, y = start
    return in_range(start) and maze[x][y] == 0


print("Masukkan posisi awal :")
while True:
    inp = input().split(" ")
    start = (int(inp[0]), int(inp[1]))
    if valid(start):
        break
    else:
        print('Input bukan blok kosong atau diluar maze')

print("Masukkan posisi akhir :")
while True:
    inp = input().split(" ")
    finish = (int(inp[0]), int(inp[1]))
    if valid(finish):
        break
    else:
        print('Input bukan blok kosong atau diluar maze')

from utils import maze, start, finish, neighbors
from collections import deque


def bfs(start, finish):  # --> [(1,2), ...]
    visited = [row[:] for row in maze]
    q = deque([(start, [start])])
    while q:
        curr, path = q.popleft()
        r, c = curr
        visited[r][c] = 1
        for r, c in neighbors(curr):
            if (r, c) == finish:
                return path + [finish]
            else:
                if visited[r][c] == 0:
                    visited[r][c] = 1
                    q.append(((r, c), path + [(r, c)]))


path = bfs(start, finish)
print(path)

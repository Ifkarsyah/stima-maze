import numpy
from heapq import *
from utils import maze, start, finish

# Fungsi heuristik berdasarkan jarak manhattan
def hn(P, Q):
    return(abs(P[0] - Q[0]) + abs(P[1] - Q[1]))


def doAStar(maze, start, finish):
    possibleMove = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    closeSet = set()
    fromPath = {}
    gn = {start: 0}
    fn = {start: hn(start, finish)}
    heapOfPath = []

    heappush(heapOfPath, (fn[start], start))

    while heapOfPath:
        currentPoint = heappop(heapOfPath)[1]
        # Cek jika sudah sampai finish
        if(currentPoint == finish):
            createdPath = []
            while(currentPoint in fromPath):
                createdPath.append(currentPoint)
                currentPoint = fromPath[currentPoint]
            createdPath.append(start)
            createdPath.reverse()
            return createdPath

        # Cari jalur berikutnya ke tetangga
        closeSet.add(currentPoint)
        for i, j in possibleMove:
            # Mencari gScore terendah dari neighbor currentPoint
            neighbor = currentPoint[0] + i, currentPoint[1] + j
            gScore = gn[currentPoint] + hn(currentPoint, neighbor)
            if(0 <= neighbor[1] < maze.shape[1]):
                if(0 <= neighbor[0] < maze.shape[0]):
                    if(maze[neighbor[0]][neighbor[1]] == 1):
                        continue # Menabrak tembok
                else:
                    continue  # Keluar dari batas x, tapi tidak y
            else:
                continue      # Keluar dari batas y
            if((neighbor in closeSet) and (gScore >= gn.get(neighbor, 0))):
                continue
            if((gScore < gn.get(neighbor, 0)) or (neighbor not in [point[1] for point in heapOfPath])):
                fromPath[neighbor] = currentPoint
                gn[neighbor] = gScore
                fn[neighbor] = gn[neighbor] + hn(neighbor, finish)
                heappush(heapOfPath, (fn[neighbor], neighbor))

jalurAStar = doAStar(numpy.array(maze), start, finish)

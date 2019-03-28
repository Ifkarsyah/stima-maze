import numpy
from heapq import *
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg
import sys

maze = []

def doBFS(start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    

def heuristic(P,Q):
    #Jarak Manhattan
    return((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)

def doAStar(array,start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

#Membaca matriks dari file teks
def readMatrix(namaFile):
    file = open(namaFile,"r")
    for line in file:
        listOfInt = list(line)
        listOfInt.pop(len(listOfInt) - 1)
        for i in range(len(listOfInt)):
            listOfInt[i] = int(listOfInt[i])
        maze.append(listOfInt)

    file.close()

#Program utama
#print("Masukkan nama berkas eksternal (tanpa kutip) :")
#namaFile = input()
namaFile = "inp.txt"
readMatrix(namaFile)
for i in maze:
    print(i)
while(True):
    print("Masukkan posisi awal :")
    inp = input().split(" ")
    awal = (int(inp[0]),int(inp[1]))
    print(awal)

    print("Masukkan posisi akhir :")
    inp = input().split(" ")
    akhir = (int(inp[0]),int(inp[1]))
    print(akhir)

    map = numpy.array(maze)

    print("Pecahkan dengan A*\n")
    jalurAStar = doAStar(map,awal,akhir)
    jalurAStar.append(awal)
    print(jalurAStar)

    ##print("Pecahkan dengan BFS\n")
    ##doBFS(awal,akhir)

    print("Apakah anda ingin mencari jalur lagi? Y/N")
    inp = input()
    if(inp == "N"):
        break

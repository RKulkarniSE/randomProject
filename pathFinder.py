import numpy as np
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0
    
def AStar(maze, start, end):
    start = Node(None, start)
    end = Node(None, end)

    open = []
    closed = []

    open.append(start)

def FCost(maze, startX, startY, endX, endY):
    print(f" starting point {maze[startY][startX]}")
    print(f" current {maze[endY][endX]}")
    print(f" F Cost {(endY - startY)**2 + (endX - startX)**2}")
    

maze = np.array([
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
# print(f" starting point {maze[0][0]}")
# print(f" current {maze[0][4]}")
# print(f" Distance {pow((16-0 + 0-0), 0.5)}")
FCost(maze, 0, 0, 3, 4)
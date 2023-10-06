import numpy as np

def GCost(maze, startX, startY, currentX, currentY):
    f_cost = (currentY - startY)**2 + (currentX - startX)**2
    return f_cost
    
def HCost(maze, endX, endY, currentX, currentY):
    h_cost = (currentY - endY)**2 + (currentX - endX)**2
    return h_cost
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
 # write a function to find the child nodes
def childNodes(maze, y, x):
    new_positions = [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0)]
    children = []
    for new_pos in new_positions:
        children.append(maze[y+new_pos[0]][x+new_pos[1]])

    return children


print(childNodes(maze, 3, 4))
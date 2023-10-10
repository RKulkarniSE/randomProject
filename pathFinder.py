import numpy as np

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    

def GCost(maze, startY, startX, currentY, currentX):
    f_cost = (currentY - startY)**2 + (currentX - startX)**2
    return f_cost
    
def HCost(maze, endY, endX, currentY, currentX):
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
def aStar(maze, y, x):
    end_node = Node(None, (7, 7))
    start_node = Node(None, (y, x))
    current_node = start_node
    new_positions = [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0)]
    open_list = []
    closed_list = []
    for new_pos in new_positions:
        if maze[y+new_pos[0]][x+new_pos[1]] != 0:
            continue
        child_node = Node(current_node, (y+new_pos[0], x+new_pos[1]))
        child_node.g += 1
        child_node.h = (end_node.position[0] - child_node.position[0]) + (end_node.position[1] - child_node.position[1])
        child_node.f = child_node.g + child_node.h
        open_list.append(child_node)

    leastCost = open_list[0] # default
    for i in range(1, len(open_list)):
        if(open_list[i].f < leastCost.f):
            leastCost = open_list[i]

    current_node = leastCost
    for node in open_list:
        if node != current_node:
            print(node.position)
            closed_list.append(node)
            open_list.remove(node)
    

    for i in open_list:
        print(f"After {i.position}")
    return open_list

print(aStar(maze, 4, 3))
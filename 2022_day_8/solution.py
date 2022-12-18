import numpy as np
from termcolor import colored
tree_list = []
with open("demo.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        tree_list.append([l for l in line.strip()])
    file.close()

trees = np.array(tree_list)
is_visible = np.zeros(trees.shape, dtype=int)

# Test case
BLOCK = '\u2588'
x = 1
y = 3

GRID_SIZE = 5
#returns array of trees between search tree & specified edge
def array_to_edge(x, y, direction):
    row = []
    print(trees[y][x])
    if direction == "right":
        for i in range(x+1,GRID_SIZE):
            row.append(trees[y][i])
            # trees[y][i] = BLOCK
            is_visible[y][i] = 1
    elif direction == "left":
        for i in range(0,x):
            row.append(trees[y][i])
            # trees[y][i] = BLOCK
            is_visible[y][i] = 1
    elif direction == "top":
        for j in range(0,y):
            row.append(trees[j][x])
            # trees[j][x] = BLOCK
            is_visible[j][x] = 1
    elif direction == "bottom":
        for j in range(y+1,GRID_SIZE):
            row.append(trees[j][x])
            # trees[j][x] = BLOCK
            is_visible[j][x] = 1

    else:
        print("Invalid direction")
    return row
    
row = array_to_edge(x,y,"top")

print(row)

# visualizing
for x in range(0,GRID_SIZE):
    row = trees[x]
    print("".join(row))
print("-----")
for x in range(0,GRID_SIZE):
    row = is_visible[x]
    for r in row:
        if r == 1:
            print(colored(r,'green'),end="")
        else:
            print(r,end="")
        
    print()
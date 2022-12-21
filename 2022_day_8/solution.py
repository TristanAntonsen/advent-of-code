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
def array_to_edge(current_tree, x, y, direction):
    row = []
    score = 0
    if direction == "right":
        for i in range(x+1,GRID_SIZE):
            tree = trees[y][i]
            row.append(tree)
            if tree >= current_tree:
                break
    elif direction == "left":
        for i in range(0,x):
            tree = trees[y][i]
            row.append(tree)
            if tree >= current_tree:
                break
    elif direction == "top":
        for j in range(0,y):
            tree = trees[j][x]
            row.append(tree)
            if tree >= current_tree:
                break
    elif direction == "bottom":
        for j in range(y+1,GRID_SIZE):
            tree = trees[j][x]
            row.append(tree)
            if tree >= current_tree:
                break
    else:
        print("Invalid direction")

    # len(row = score)
    return row, len(row)
    

## Visibility loop
visible_count = 0
highest_score = 0
highest_score_pos = [0,0]
highest_score_height = 0

for x in range(0,GRID_SIZE):
    for y in range(0,GRID_SIZE):
        current_tree = trees[y][x]
        dirs = ["right","left","top","bottom"]
        scores = []
        visibility = []
        for dir in dirs:
            arr, dir_score = array_to_edge(current_tree, x, y, dir)
            v = True
            for t in arr:
                v = v and (int(current_tree) > int(t))
            visibility.append(v)
            scores.append(dir_score)

        score = np.product(scores)
        
        if score > highest_score:
            highest_score = score
            highest_score_pos = [y,x]
            highest_score_height = current_tree

        if True in visibility:
            is_visible[y][x] = 1
            visible_count += 1

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

print("-----")
    
for x in range(0,GRID_SIZE):
    row = is_visible[x]
    for i, r in enumerate(row):
        if [x,i] == highest_score_pos:
            print(colored(trees[x][i],'red'),end="")
        elif r == 1:
            print(colored(trees[x][i],'green'),end="")
        else:
            print(trees[x][i],end="")
    print()
print("Visible:",visible_count)
print("Highest score: ",highest_score)
print("Highest score position: ",highest_score_pos)
print("Highest score height: ",highest_score_height)
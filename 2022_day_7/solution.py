from pprint import pprint
import sys

input_file = sys.argv[1]

with open(input_file,"r") as file:
    lines = file.readlines()
    file.close()

directories = {}
current_directory = "/"
last_directory = "/"
directories["/"] = {
    'children' : [],
    'total_size' : 0,
    'size' : 0
}
for i in range(len(lines)):
    current_line = lines[i].strip().split(" ")
    type = current_line[0]

    # Case 1: User command (getting current directory)
    if type == "$":
        cmd = current_line[1]
        if cmd == "cd": # if changing directories
            if current_line[-1] != "..": # if entering a directory
                target_directory = current_line[-1] 
                last_directory = current_directory
            else: # if stepping back a directory
                target_directory = last_directory # set 
                last_directory = current_directory

            current_directory = target_directory
        else:
            continue
    
    else:
        if current_directory in directories.keys():
            directories[current_directory]["children"].append(current_line)
        else:
            directories[current_directory] = {
                'children' : [current_line],
                'size' : 0
            }

# pprint(directories)
directory_names = list(directories.keys())
# for dir in directory_names:
#     print(dir)
#     for child in directories[dir]['children']:
#         print(" "," ".join(child))

# step 1, add file sizes to directories

for dir in directory_names:
    for child in directories[dir]['children']:
        type = child[0]
        file = child[1]
        if type != "dir":
            size = int(child[0])
            directories[dir]['size'] += size
        
# step 2, add directory sizes to directories
for dir in directory_names:
    for child in directories[dir]['children']:
        type = child[0]
        file = child[1]
        if type == "dir":
            size = directories[file]['size']
            directories[dir]['size'] += size

# step 3,count directories above threshold & sum
running_sum = 0
for dir in directory_names:
    size = directories[dir]['size']
    if size <= 100000:
        running_sum += size
    # print("dir: ",directories[dir]['size'])
    # if len(directories[dir]['children']) < 1:
    #     print(directories[dir])

pprint(directories)
print("Total of sizes <= 100000:",running_sum)

# Demo Hierarchy:
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)


# might work but hits max recursion depth
# def recursive_size_calc(directory):

#     for child in directories[directory]['children']:
#         type = child[0]
#         file = child[1]
#         if type != "dir":
#             size = int(child[0])
#             directories[directory]['size'] += size
#         else:
#             # print(file, directories[file]['children'])
#             recursive_size_calc(file)
#             directories[directory]['size'] += directories[file]['size']

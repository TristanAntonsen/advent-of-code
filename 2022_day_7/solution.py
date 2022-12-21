from pprint import pprint

with open("demo_input.txt","r") as file:
    lines = file.readlines()
    file.close()

directories = {}
current_directory = "/"
last_directory = "/"
directories["/"] = {
    'parent': '',
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
        if cmd == "cd":
            if current_line[-1] != "..":
                target_directory = current_line[-1]
                last_directory = current_directory
            else:
                target_directory = last_directory
                last_directory = current_directory

            current_directory = target_directory
        else:
            continue

        if current_directory in directories.keys():
            directories[current_directory] = {
                "parent" : last_directory
            }
            
    print("last:",last_directory,"current:", current_directory, current_line)



## Calculating sizes of files in directories
## not counting child directories
# for d in directories.keys():
#     dir = directories[d]
#     size = sum([int(c[0]) for c in dir['children']])
#     directories[d]['size'] = size

## Summing total sizes of directories

# def recursive_sum(directory):

#     for child in directory['children']:
#         print(child)
#         if child[0] == "dir":
#             print(child)
#             recursive_sum(directories[child[-1]])
#         else:
#             directory['total_size'] += int(child[0])

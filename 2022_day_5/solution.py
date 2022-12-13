from pprint import pprint

STACKS = [['Z', 'J', 'G'],
          ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
          ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
          ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
          ['G', 'C', 'F', 'S', 'V', 'Q'],
          ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
          ['H', 'F', 'S', 'B', 'V'],
          ['F', 'J', 'Z', 'S'],
          ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']]

def move_crate(start_stack, end_stack):
        # crate being moved
        print(start_stack, end_stack)
        crate = start_stack[-1]
        # adding crates to new stack
        end_stack.append(crate)
        start_stack.pop(-1)

        

with open('input.txt','r') as file:
    lines = file.readlines()

    for line in lines:
        instructions = line.strip().split(" ")
        move_count = int(instructions[1])
        move_from = int(instructions[3]) - 1
        move_to = int(instructions[5]) - 1
        for i in range(0,move_count):
            move_crate(STACKS[move_from], STACKS[move_to])

top_crates = "".join([s[-1] for s in STACKS])

print(top_crates)
print(len(top_crates))

# WFRHTFFBF wrong
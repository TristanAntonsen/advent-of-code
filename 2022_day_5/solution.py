import time
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

moved_stacks = STACKS

def move_crate(start_stack, end_stack):
        # crate being moved
        crate = start_stack[-1]
        # adding crates to new stack
        end_stack.append(crate)
        start_stack.pop(-1)

def move_crates(stacks, start, end, count):
        # crates being moved
        start_stack = stacks[start]
        end_stack = stacks[end]
        crates = start_stack[-count:]
        # adding crates to new stack
        end_stack = end_stack + crates
        start_stack = start_stack[:-count]
        stacks[start] = start_stack
        stacks[end] = end_stack
        
def visualize_stacks(stacks):
        
        for i, stack in enumerate(stacks):
                pretty_stack = ''.join(stack)
                print(f"({i}) {pretty_stack}")
        print("==========")

with open('input.txt','r') as file:
        lines = file.readlines()

        for line in lines:
                instructions = line.strip().split(" ")
                move_count = int(instructions[1])
                move_from = int(instructions[3]) - 1
                move_to = int(instructions[5]) - 1
                # for i in range(0,move_count):
                #     move_crate(moved_stacks[move_from], moved_stacks[move_to])
                move_crates(moved_stacks, move_from, move_to, move_count)
top_crates = ''.join([s[-1] for s in moved_stacks])
print(top_crates)
# WFRHTFFBF wrong
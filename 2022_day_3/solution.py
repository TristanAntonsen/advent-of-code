import string

PRIORITIES = dict((i, j+1) for j, i in enumerate(string.ascii_letters))


with open('input.txt','r') as file:
    lines = file.readlines()

    priority_sum = 0
    for line in lines:
        line = line.strip()
        item_count = int(len(line) / 2)
        comp_1 = sorted(line[:item_count])
        comp_2 = sorted(line[item_count:])

        common = set(comp_1) & set(comp_2)
        priority = PRIORITIES[list(common)[0]]
        priority_sum += priority

print(priority_sum)
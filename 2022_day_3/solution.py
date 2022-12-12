import string

PRIORITIES = dict((i, j+1) for j, i in enumerate(string.ascii_letters))


with open('input.txt','r') as file:
    lines = file.readlines()

    priority_sum = 0
    # PART 1:
    # for line in lines:
    #     line = line.strip()
    #     item_count = int(len(line) / 2)
    #     comp_1 = sorted(line[:item_count])
    #     comp_2 = sorted(line[item_count:])

    #     common = set(comp_1) & set(comp_2)
    #     priority = PRIORITIES[list(common)[0]]
    #     priority_sum += priority

    # PART 2:
    i = 0
    while i < len(lines):
        bag_1 = lines[i].strip()
        bag_2 = lines[i + 1].strip()
        bag_3 = lines[i + 2].strip()

        common = set(bag_1) & set(bag_2) & set(bag_3)
        priority = PRIORITIES[list(common)[0]]
        priority_sum += priority
        i += 3

print(priority_sum)
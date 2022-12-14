with open('input.txt','r') as file:
    lines = file.readlines()

    contained_sets = 0
    overlapping_sets = 0

    sets = []

    for line in lines:

        line = line.strip()
        elves = line.strip().split(",")
        e1 = elves[0].split("-")
        e2 = elves[1].split("-")

        e1_min = int(e1[0])
        e1_max = int(e1[-1])
        e2_min = int(e2[0])
        e2_max = int(e2[-1])

        # check for edge case where ranges are equal
        if e1_min != e2_min or e1_max != e2_max:

            ### Contained
            if e1_min >= e2_min and e1_max <= e2_max:
                contained_sets += 1
                # print(e1, e2)
            if e2_min >= e1_min and e2_max <= e1_max:
                contained_sets += 1
                # print(e1, e2)
            
        # only add 1 for case where identical
        else:
            contained_sets += 1

        elf1 = set(range(e1_min, e1_max + 1))
        elf2 = set(range(e2_min, e2_max + 1))

        union = elf1 & elf2
        if len(list(union)) > 0:
            overlapping_sets += 1


    print(contained_sets)
    print(overlapping_sets)
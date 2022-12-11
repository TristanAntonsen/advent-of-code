with open("input.txt",'r') as file:
    lines = file.readlines()
    counter = 0
    last_max = 0
    total_elves = 0
    for line in lines:
        try:
            line_cals = int(line)
            counter += line_cals
        except:
            if counter > last_max:
                last_max = counter
            total_elves += 1
            counter = 0
        
print(f"Total elves: {total_elves}")
print(f"Max calories: {last_max}")
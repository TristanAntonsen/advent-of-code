# # PART 1
# with open("input.txt",'r') as file:
#     lines = file.readlines()
#     counter = 0
#     last_max = 0
#     total_elves = 0
#     for line in lines:
#         try:
#             line_cals = int(line)
#             counter += line_cals
#         except:
#             if counter > last_max:
#                 last_max = counter
#             total_elves += 1
#             counter = 0

# PART 2
with open("input.txt",'r') as file:
    lines = file.readlines()
    counter = 0
    total_elves = 0
    cal_list = []
    for line in lines:
        try:
            line_cals = int(line)
            counter += line_cals
        except:
            cal_list.append(counter)
            total_elves += 1
            counter = 0
    top_three = sorted(cal_list)[-3:]
        
print(f"Total elves: {total_elves}")
print(f"Top 3: {top_three}")

# print(f"Max calories: {last_max}")
print(f"Top three sum: {sum(top_three)}")
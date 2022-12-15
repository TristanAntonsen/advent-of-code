import os
with open('input.txt','r') as file:
    input = file.read()
    file.close()

def first_four(str):

    for i in range(3,len(str)):
        four = str[i - 3] + str[i - 2] + str[i - 1] + str[i]
        if len(set(four)) == 4:
            return i + 1


index = first_four(input)
print(input[index-4:index])
print(index)
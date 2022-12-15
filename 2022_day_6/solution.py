import os
with open('input.txt','r') as file:
    input = file.read()
    file.close()

def first_four(str, unique_count):

    for i in range(3,len(str)):

        buff = str[i-unique_count:i]

        if len(set(buff)) == unique_count:
            return i

unique = 14
index = first_four(input, unique)
print(input[index-unique:index])
print(index)
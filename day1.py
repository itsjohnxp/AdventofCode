"""
Created by John Nguyen
"""


a_list = []
b_list = []

"""
Import the input as a text file
Strip out \n
Create separate list of int and operators
"""

with open('text.txt') as f:
    for line in f:
        line = line.strip()
        a_list.append(line[1:])
        b_list.append(line[0])


#Loop through and calculates the output
num = 0
ind = 0 
for item in b_list:
    if b_list[ind] is '+':
        num += int(a_list[ind])
        ind += 1
    else:
        num -= int(a_list[ind])
        ind += 1

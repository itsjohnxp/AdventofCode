double = 0
triple = 0
new_dict = {}
dict2 = {}
dict3 = {}


with open('day2.txt') as f:
    for line in f:
        line = line.strip()
        for item in line:
            new_dict[line] = {char:line.count(char) for char in line}
            
for title in new_dict:
    for key in title:
        if new_dict[title][key] == 2:
            dict2[title] = 2
        if new_dict[title][key] == 3:
            dict3[title] = 3

for item in dict2:
    double += 1
for item in dict3:
    triple += 1
           
print(double * triple)

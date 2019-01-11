# coding: utf-8

lines = open('all_features.txt', 'r').readline().split(', ')
f_dict = {}

for line in lines:

    if f_dict.has_key(line) == False:
        f_dict[line] = 1
    else:
        print(line)
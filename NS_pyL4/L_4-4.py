my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_dict = {i: 0 for i in my_list}

for i in my_list:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])

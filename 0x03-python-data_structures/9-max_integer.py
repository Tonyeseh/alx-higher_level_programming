#!usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_num = my_list[0]
    for i in range(1, len(my_list) - 1):
        if max_num < my_list[i]:
            max_num = my_list[i]
    return max_num

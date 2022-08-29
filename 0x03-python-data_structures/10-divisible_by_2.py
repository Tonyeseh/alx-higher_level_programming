#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    if my_list is not None or len(my_list) != 0:
        for i in my_list:
            if i % 2 == 0:
                res += [True]
            else:
                res += [False]
    return (res)

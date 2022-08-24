#!/usr/bin/python3
for num in range(10):
    for num1 in range(10):
        if num is not 9 or num1 is not 9:
            print("{}{}".format(num, num1), end=', ')
        else:
            print("{}{}".format(num, num1))

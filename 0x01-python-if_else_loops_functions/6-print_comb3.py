#!/usr/bin/python3
i = 0
while i < 9:
    j = i + 1
    while j < 10:
        print(f"{i}", end='')
        print(f"{j}", end='')
        if i == 8 and j == 9:
            print("")
        else:
            print("", end=", ")
        j += 1
    i += 1

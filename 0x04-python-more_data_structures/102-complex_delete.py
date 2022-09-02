#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst = []
    for key, pair in a_dictionary.items():
        if pair == value:
            lst += [key]
    for i in lst:
        del a_dictionary[i]
    return (a_dictionary)

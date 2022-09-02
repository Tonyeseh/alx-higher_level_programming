#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        max_score = -1
        for i in a_dictionary:
            if max_score < a_dictionary[i]:
                best = i
                max_score = a_dictionary[i]
        return best

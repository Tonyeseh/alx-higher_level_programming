#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer
    """
    if type(roman_string) is str and roman_string is not None:
        prev_i = ""
        num = 0
        for i in roman_string:
            if i == "M":
                if prev_i == "C": num += 800
                else: num += 1000
            elif i == "D":
                if prev_i == "C": num += 300
                else: num += 500
            elif i == "C":
                if prev_i == "X": num += 80
                else: num += 100
            elif i == "L":
                if prev_i == "X": num += 30
                else: num += 50
            elif i == "X":
                if prev_i == "I": num += 8
                else: num += 10
            elif i == "V":
                if prev_i == "I": num += 3
                else: num += 5
            elif i == "I":
                num += 1
            else:
                return (0)
            prev_i = i
        return (num)
    return (0)

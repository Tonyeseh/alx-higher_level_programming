#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XLVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CMVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

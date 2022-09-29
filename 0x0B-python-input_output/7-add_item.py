#!/usr/bin/python3
""" Script that adds all arguments to a python lsit and then
save them to a file """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
for arg in range(1, len(sys.argv)):
    my_list.append(sys.argv[arg])

try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []
lst += my_list
save_to_json_file(lst, "add_item.json")

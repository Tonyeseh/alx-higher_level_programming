#!/usr/bin/python3
""" Module defines ``read_file(filename)`` function """

def read_file(filename=""):
    """ opens a file and prints it's content out

        Args:
            filename (string): file name to open sometimes with path.

    """
    with open(filename, encoding="utf-8") as f:
        file_data = f.read()
        print(file_data, end="")

#!/usr/bin/python3
""" Defines ``append_write()`` function"""


def append_write(filename="", text=""):
    """ appends astring at the end of a text file UTF-8

        Args:
            filename (string): name of file, sometimes contains path
            text (string): text to add to file

        Returns: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        num_of_char = f.write(text)
        return (num_of_char)

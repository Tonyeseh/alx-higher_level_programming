#!/usr/bin/python3
""" Defines write_file(...) function """


def write_file(filename="", text=""):
    """ writes to a string to a text file

        Args:
            filename (string): name of file
            text (string): string to write to file ``filename``

        Returns: Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_of_char = f.write(text)
        return (num_of_char)

#!/usr/bin/python3
""" Defines ``append_after()`` function """

def append_after(filename="", search_string="", new_string=""):
    """ inserts a new line of text to a file, after each line containing a specific string

        Args:
            search_string (str): string to search for
            new_string (str): string to insert

    """
    if search_string != "" or new_string != "":
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(filename, "w", encoding="utf-8") as fw:
            s = ""
            for line in lines:
                s += line
                if search_string in line:
                    s += new_string
            fw.write(s)

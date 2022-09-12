#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as err:
        error_msg = "Exception: " + str(err) + "\n"
        sys.stderr.write(error_msg)
        return (False)


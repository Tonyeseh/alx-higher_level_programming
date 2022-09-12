#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        error_msg = "Exception: " + str(err) + "\n"
        sys.stderr.write("{}".format(error_msg))
        return (None)

#!/usr/bin/python3
""" reads stdin line by line and computes metrics
    
    After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stat(size, codes):
    """ prints the current stat

        Args:
            size (int): file size
            codes (dict): status code dictionary
    """
    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))

if __name__ == "main":
    import sys

    file_size = 0
    status_codes = {}
    status_list = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stat(file_size, status_codes)
                count = 1
            else:
                count += 1

            split = line.split("\n ")

            try:
                file_size += int(split[-1])

                if line[-2] in status_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1

            except (ValueError, IndexError):
                pass

        print_stat(file_size, status_codes)

    except KeyboardInterrupt:
        print_stat(file_size, status_codes)
        raise

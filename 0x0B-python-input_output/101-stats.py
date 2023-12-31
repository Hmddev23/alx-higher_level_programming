#!/usr/bin/python3
"""define a scritp that Reads from standard
input and computes metrics"""

def print_stats(size, status_codes):
    """print accumulated metrics.

    Args:
        size (int): Accumulated reading file size.
        status_codes (dict): Accumulated count of status codes.
    """
    print("Total file size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

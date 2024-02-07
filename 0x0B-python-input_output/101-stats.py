#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_info(file_size, status_codes):
    """Print file size and status codes.

    Args:
        file_size (int): Accumulated file size.
        status_codes (dict): Accumulated status codes count.
    """
    print("File size: {:d}".format(file_size))

    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {:d}".format(code, count))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            try:
                file_size += int(line.split()[-1])
            except (ValueError, IndexError):
                pass

            try:
                status_code = line.split()[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_info(file_size, status_codes)

        print_info(file_size, status_codes)

    except KeyboardInterrupt:
        print_info(file_size, status_codes)
        raise

#!/usr/bin/python3

import sys


def print_statistics(total_size, status_counts):
    """
    Prints the computed statistics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def parse_line(line, total_size, status_counts):
    """
    Parses a log line and updates total file size and status code counts.

    Args:
        line (str): The log line to parse.
        total_size (int): The total file size.
        status_counts (dict): Dictionary to store counts of status codes.
    """
    parts = line.split()
    if len(parts) != 10 or not parts[8].isdigit():
        return

    status_code = int(parts[8])
    file_size = int(parts[9])

    total_size += file_size
    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    return total_size


def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            total_size = parse_line(line.strip(), total_size, status_counts)
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()

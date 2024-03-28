#!/usr/bin/python3

import sys

def print_statistics(total_size, status_counts):
    """
    Print computed statistics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """
    Parse a log line.

    Args:
        line (str): Log line to parse.

    Returns:
        tuple: (file_size, status_code) if successful, else None.
    """
    parts = line.split()
    if len(parts) != 10:
        return None

    try:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        return (file_size, status_code)
    except ValueError:
        return None

def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_line(line)
            if parsed:
                file_size, status_code = parsed
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

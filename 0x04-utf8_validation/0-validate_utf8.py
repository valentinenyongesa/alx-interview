#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    # Number of bytes for each character, indexed by the first byte
    byte_lengths = {
        0: 1,
        1: 2,
        2: 2,
        3: 3,
        4: 4
    }

    # Number of bytes to skip after the current character
    skip_bytes = 0

    for num in data:
        # If we're skipping bytes, decrement the skip count
        if skip_bytes > 0:
            skip_bytes -= 1
            continue

        # Determine the length of this character based on the first byte
        if num >> 7 == 0:
            length = 1
        elif num >> 5 == 6:
            length = 2
        elif num >> 4 == 14:
            length = 3
        elif num >> 3 == 30:
            length = 4
        else:
            return False

        # Verify that the following bytes start with the correct bit pattern
        for i in range(1, length):
            if len(data) <= i:
                return False
            if data[data.index(num) + i] >> 6 != 2:
                return False

        # Update skip_bytes
        skip_bytes = byte_lengths[length] - 1

    return True


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

#!/usr/bin/python3
"""
Module for calculating minimum operations to reach n characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format
          (n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format
          (n, minOperations(n)))

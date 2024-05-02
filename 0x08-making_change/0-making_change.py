#!/usr/bin/python3
"""
Module for making change.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin values.
        total (int): Total amount to reach.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if impossible.
    """
    if total < 1:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

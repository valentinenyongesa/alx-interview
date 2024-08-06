#!/usr/bin/python3


def sieve_of_eratosthenes(limit):
    """Generate a list of primes up to `limit`."""
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine the winner of the most rounds of the Prime Game."""
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        turn = 0  # Maria starts first
        # Available numbers from 1 to n
        available = [True] * (n + 1)
        available[0] = False  # 0 is not part of the game

        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                # Remove this prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                turn = 1 - turn  # Switch turns

        if turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

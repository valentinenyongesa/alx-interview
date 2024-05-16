#!/usr/bin/python3


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if sieve[p]:
            primes.append(p)
            for i in range(p**2, n + 1, p):
                sieve[i] = False
        p += 1
    for p in range(p, n + 1):
        if sieve[p]:
            primes.append(p)
    return primes


def simulate_round(nums):
    primes = sieve_of_eratosthenes(max(nums))
    for prime in primes:
        nums = [num for num in nums if num % prime != 0 or num == prime]
        if not nums:
            return "Maria" if prime in nums else "Ben"
    return "Maria"


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        winner = simulate_round(list(range(1, nums[i] + 1)))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

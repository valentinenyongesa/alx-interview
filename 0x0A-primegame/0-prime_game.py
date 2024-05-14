#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def play_round(primes, n):
    if n <= 1:
        return None  # No prime numbers to choose
    for prime in primes:
        if prime <= n and n % prime == 0:
            return "Ben"
    return "Maria"

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    primes = generate_primes(max(nums))
    for n in nums:
        winner = play_round(primes, n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if ben_wins > maria_wins:
        return "Ben"
    else:
        return "Maria"

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

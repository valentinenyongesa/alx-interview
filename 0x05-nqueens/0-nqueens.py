#!/usr/bin/python3
"""N queens puzzle"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if (board[i] == row or
                board[i] - i == row - col or
                board[i] + i == row + col):
            return False
    return True


def solve_nqueens(n, board, col, solutions):
    """Recursively find all solutions to N queens problem"""
    if col == n:
        solutions.append(board[:])
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(n, board, col + 1, solutions)


def print_solutions(n, solutions):
    """Print solutions to the N queens problem"""
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(N, solutions)


if __name__ == "__main__":
    main()

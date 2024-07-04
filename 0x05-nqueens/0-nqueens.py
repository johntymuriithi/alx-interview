#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Solve the N queens problem using backtracking"""
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)


def print_solutions(solutions):
    """Print the solutions in the required format"""
    for solution in solutions:
        print([[i, col] for i, col in enumerate(solution)])


def main():
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

    solutions = []
    solve_nqueens(N, 0, [-1] * N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

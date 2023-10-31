#!/usr/bin/python3
"""Solves the N-Queens problem."""


import sys


def initialize_board(size):
    """Initializes an 'size' x 'size' chessboard with empty spaces."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

def deepcopy_board(board):
    """Returns a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [deepcopy_board(row) for row in board]
    return board

def find_queen_positions(board):
    """Returns a list of positions of queens on the chessboard."""
    positions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                positions.append([row, col])
                break
    return positions

def mark_attacked_spots(board, row, col):
    """Marks spots on the chessboard attacked by a queen."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"  # X out all forward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # X out all backwards spots
    for r in range(row + 1, len(board)):
        board[r][col] = "x"  # X out all spots below
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # X out all spots above

    # Diagonal movements
    r, c = row + 1, col + 1
    while r < len(board) and c < len(board[0]):
        board[r][c] = "x"  # X out diagonally down to the right
        r += 1
        c += 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"  # X out diagonally up to the left
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < len(board[0]):
        board[r][c] = "x"  # X out diagonally up to the right
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < len(board) and c >= 0:
        board[r][c] = "x"  # X out diagonally down to the left
        r += 1
        c -= 1

def solve_nqueens(board, row, queens, solutions):
    """Recursively solves an N-Queens puzzle.

    Args:
        board (list): Current working chessboard.
        row (int): Current working row.
        queens (int): Number of placed queens.
        solutions (list): List of solutions.

    Returns:
        solutions of the game.
    """
    if queens == len(board):
        solutions.append(find_queen_positions(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = deepcopy_board(board)
            tmp_board[row][col] = "Q"
            mark_attacked_spots(tmp_board, row, col)
            solutions = solve_nqueens(tmp_board, row + 1, queens + 1, solutions)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(n)
    solutions = solve_nqueens(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)

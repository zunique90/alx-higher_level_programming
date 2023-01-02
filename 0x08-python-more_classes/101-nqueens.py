#!/usr/bin/python3
"""a program that solves the N queens problem."""


import sys


def board_init(n):
    """initializes an n x n sized chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return board


def board_deepcpy(board):
    """returns a deep copy of a chessboard."""
    if type(board) is list:
        return list(map(board_deepcpy, board))
    return board


def get_sol(board):
    """Returns the list of lists representation of a solved chessboard."""
    sol = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                sol.append([r, c])
                break
    return sol


def xout(board, row, col):
    """
    x-out all spots where non-attacking queen can no longer play
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_sol(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_deepcpy(board)
            temp_board[row][c] = "Q"
            xout(temp_board, row, c)
            solutions = recursive_solve(
                    temp_board, row + 1, queens + 1, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = board_init(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)

#!/usr/bin/python3
"""
nqueen module
"""
import sys

board = []
queensIncice = []


def is_safe(x, y):
    """
    check if positoin is at risk
    """
    for i in range(y):
        if board[x][i] == 1:
            return False

    for i, j in zip(range(x, len(board)), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def sloveNqueen(y):
    """
    function that solve the problem
    """
    size = len(board)
    if y == size:
        correctPos = [[i, j] for i in range(size)
                      for j in range(size) if board[i][j] == 1]
        queensIncice.append(correctPos)
        return True
    else:
        for x in range(size):
            if is_safe(x, y):
                board[x][y] = 1
                sloveNqueen(y + 1)
                board[x][y] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens size")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("size must be a number")
        exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print("size must be at least 4")
        sys.exit(1)

    board = [[0] * size for i in range(size)]
    sloveNqueen(0)
    for correctPos in queensIncice:
        print(correctPos)

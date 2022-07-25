#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


class Solution:
    col = set()
    positive_diag = set()  # (r + c)
    negative_diag = set() # (r - c)
    result = []
 
    def __init__(self, n: int):
        self__n = n

    def SolveQueens(self):
        board = [["."] * n for i in range(n)]

        """ def init_board(n):
            board = []
            [board.append([]) for i in range(n)]
            [row.append(' ') for i in range(n) for row in board]
            return (board)
        """

        def backtrack(r):
            if (r == n):
                copy = [".".join(row) for row in board]
                result.append(copy)
                return (0)

            for c in range(n):
                if c in col or (r + c) in positive_diag or (r - c) in negative_diag:
                    continue
                col.add(c)
                positive_diag.add(r + c)
                negative_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return (result)
    

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

    #board = init_board(int(sys.argv[1]))
    solutions = Solution(int(sys.argv[1])
    sol = solutions.SolveQueens()
    print(sol)

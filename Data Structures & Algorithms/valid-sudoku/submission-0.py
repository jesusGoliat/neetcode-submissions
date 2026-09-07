from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        row_set = [set() for _ in range(row)]
        col_set = [set() for _ in range(col)]
        square_set = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(row):
            for j in range(col):
                x = board[i][j]
                if x == '.':
                    continue
                if x in row_set[i] or x in col_set[j] or x in square_set[i//3][j//3]:
                    return False
                row_set[i].add(x)
                col_set[j].add(x)
                square_set[i//3][j//3].add(x)
        return True
                
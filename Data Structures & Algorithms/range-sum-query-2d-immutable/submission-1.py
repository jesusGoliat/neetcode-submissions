from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        # Add an extra row and column of 0s to avoid out-of-bounds checks
        self.prefix = [[0] * (col + 1) for _ in range(row + 1)]
        
        # Build the 2D prefix sum array in a single pass O(M * N)
        for i in range(1, row + 1):
            row_sum = 0
            for j in range(1, col + 1):
                # 1. Add current cell to the running row sum
                row_sum += matrix[i-1][j-1]
                # 2. 2D area = current row sum + 2D area from the row directly above
                self.prefix[i][j] = row_sum + self.prefix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate O(1) area using the inclusion-exclusion principle
        total = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return total
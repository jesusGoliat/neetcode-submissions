class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row =  len(matrix)
        col = len(matrix[0])
        self.prefix = [[0]*(col+1) for _ in range(row+1)]
        #We copy the matrix
        for i in range(row):
            for j in range(col):
                self.prefix[i+1][j+1] = matrix[i][j]
        #We make a prefix sum by row:
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.prefix[i][j] += self.prefix[i][j-1]
        #We make a prefix sum by col:
        for i in range(1,col+1):
            for j in range(1,row+1):
                self.prefix[j][i] += self.prefix[j-1][i]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return total
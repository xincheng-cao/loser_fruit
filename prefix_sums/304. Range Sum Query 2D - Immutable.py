class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        vec = []
        for i in range(len(matrix)):
            vec.append([0] * len(matrix[0]))

        vec[0][0] = matrix[0][0]
        for i in range(1, len(matrix[0])):
            vec[0][i] = vec[0][i - 1] + matrix[0][i]
        for i in range(1, len(matrix)):
            vec[i][0] = vec[i - 1][0] + matrix[i][0]

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                sum_diag = vec[row - 1][col - 1]
                sum_left = vec[row][col - 1]
                sum_up = vec[row - 1][col]

                vec[row][col] = sum_left + sum_up - sum_diag + matrix[row][col]
        self._vec = vec
        print(self._vec)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 >= 1 and col1 >= 1:
            sum_diag = self._vec[row1 - 1][col1 - 1]
        else:
            sum_diag = 0

        if col1 >= 1:
            sum_left = self._vec[row2][col1 - 1]
        else:
            sum_left = 0

        if row1 >= 1:
            sum_up = self._vec[row1 - 1][col2]
        else:
            sum_up = 0
        return self._vec[row2][col2] - sum_left - sum_up + sum_diag

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
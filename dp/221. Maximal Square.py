class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] == '1':
                        return 1
            return 0
        else:
            max_ans = 0
            for row in range(1):
                for col in range(len(matrix[0])):
                    if matrix[row][col] == '1':
                        max_ans = 1
                        break
            for row in range(len(matrix)):
                for col in range(1):
                    if matrix[row][col] == '1':
                        max_ans = 1
                        break
        # print(max_ans)

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == '1':
                    matrix[row][col] = str(
                        min(int(matrix[row][col - 1]), int(matrix[row - 1][col]), int(matrix[row - 1][col - 1])) + 1)
                    max_ans = max(max_ans, int(matrix[row][col]))
        # print(matrix)
        return max_ans ** 2

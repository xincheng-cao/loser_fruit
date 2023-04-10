class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def convert_1d_to_2d(idx: int):
            row = idx // len(matrix[0])
            col = idx % len(matrix[0])
            return row, col

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = convert_1d_to_2d(mid)
            print(row, col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:

                left = mid + 1
        return False








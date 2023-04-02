import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k == 1:
            return matrix[0][0]

        seen = {(0, 0)}
        li = [(matrix[0][0], 0, 0)]
        heapq.heapify(li)
        # ans=None
        for i in range(1, k):
            _, row, col = heapq.heappop(li)
            # print(ans,row,col)
            # if i ==k-1:break

            if row + 1 < len(matrix) and (row + 1, col) not in seen:
                heapq.heappush(li,
                               (matrix[row + 1][col], row + 1, col)
                               )
                seen.add((row + 1, col))

            if col + 1 < len(matrix[0]) and (row, col + 1) not in seen:
                heapq.heappush(
                    li,
                    (matrix[row][col + 1], row, col + 1)
                )
                seen.add((row, col + 1))
        return heapq.heappop(li)[0]









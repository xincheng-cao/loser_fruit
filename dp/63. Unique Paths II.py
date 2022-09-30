from operator import neg


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = []
        for i in range(m):
            res.append(list(map(neg, obstacleGrid[i])))

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if res[i][j] == -1:
                        return 0
                    else:
                        res[i][j] = 1
                elif i >= 1 and j >= 1:
                    if res[i][j] == -1:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i - 1][j] + res[i][j - 1]
                elif i == 0:
                    if res[i][j] == -1:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i][j - 1]
                else:
                    if res[i][j] == -1:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i - 1][j]
        return res[m - 1][n - 1]
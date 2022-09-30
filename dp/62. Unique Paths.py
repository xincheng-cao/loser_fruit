class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[[1]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i>=1 and j>=1:
                    res[i][j]=res[i-1][j]+res[i][j-1]
                elif i==0:
                    res[i][j]=res[i][j-1]
                else:
                    res[i][j]=res[i-1][j]
        return res[m-1][n-1]
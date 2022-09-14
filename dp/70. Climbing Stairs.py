class Solution:
    def climbStairs(self, n: int) -> int:
        #dp
        res=[0,1,2]
        if n>=3:
            for i in range(3,n+1):
                a=res[i-1]
                b=res[i-2]
                res.append(a+b)
        return res[n]
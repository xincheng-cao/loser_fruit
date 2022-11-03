class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        f(0)=1
        f(1)=10
        f(2)=9*9+f(1)
        f(3)=9*9*8+f(2)
        f(4)=9*9*8*7+f(3)
        '''
        if n == 0: return 1
        if n == 1: return 10
        res = 10

        for i in range(n - 1):
            temp_res = 9
            for j in range(i + 1):
                temp_res *= (9 - j)
            res += temp_res
        return res

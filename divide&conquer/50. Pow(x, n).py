class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            flag = False
        else:
            flag = True

        n = abs(n)
        op = []

        while n > 1:
            if n % 2 == 1:
                n -= 1
                op.append(1)
            else:
                n = n // 2
                op.append(2)
        # n==1
        res = x

        while len(op) > 0:
            if op.pop() == 1:
                res = res * x
            else:
                res = res * res

        if not flag:
            res = 1 / res

        return res

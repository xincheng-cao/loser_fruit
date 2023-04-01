import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        p2 = 0
        p3 = 0
        p5 = 0
        li = [1]
        for i in range(2, n + 1):
            li.append(
                min(li[p2] * 2, li[p3] * 3, li[p5] * 5,
                    )
            )
            if li[-1] == li[p2] * 2:
                p2 += 1
            if li[-1] == li[p3] * 3:
                p3 += 1
            if li[-1] == li[p5] * 5:
                p5 += 1
        return li[-1]


import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        seen = {1}
        li = [1]
        heapq.heapify(li)
        ans = None
        for i in range(2, n + 1):
            smallest = heapq.heappop(li)
            if 2 * smallest not in seen:
                heapq.heappush(li, smallest * 2)
                seen.add(smallest * 2)

            if 3 * smallest not in seen:
                heapq.heappush(li, smallest * 3)
                seen.add(smallest * 3)
            if 5 * smallest not in seen:
                heapq.heappush(li, smallest * 5)
                seen.add(smallest * 5)
            ans = li[0]
            # print(li)
        return ans

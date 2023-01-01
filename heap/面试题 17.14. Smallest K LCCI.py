import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == arr.__len__():
            return arr

        arr_rev = []
        for e in arr:
            arr_rev.append(-1 * e)

        max_h = arr_rev[:k]
        heapq.heapify(max_h)

        for i in range(k, len(arr)):
            heapq.heappushpop(max_h, arr_rev[i])

        res = []
        for e in max_h:
            res.append(-1 * e)
        return res

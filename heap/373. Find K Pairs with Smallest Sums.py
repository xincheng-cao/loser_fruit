from heapq import heappop,heappush

class Solution:
    def kSmallestPairs(self, nums1, nums2 , k: int) :
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

s=Solution()
s.kSmallestPairs([1,7,11],[2,4,6,],3)
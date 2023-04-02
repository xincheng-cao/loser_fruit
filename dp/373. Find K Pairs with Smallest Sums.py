import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k=min(k,len(nums1)*len(nums2))

        if k==0:return []
        li=[(nums1[0]+nums2[0],0,0)]
        seen=set((0,0))
        ans=[]
        heapq.heapify(li)
        for i in range(k):
            temp=heapq.heappop(li)
            ans.append([nums1[temp[1]],nums2[temp[2]]])
            #go right
            if temp[2]+1<len(nums2) and (temp[1],temp[2]+1) not in seen:
                seen.add((temp[1],temp[2]+1))
                heapq.heappush(li,(nums1[temp[1]]+nums2[temp[2]+1],temp[1],temp[2]+1))
            # go down
            if temp[1]+1<len(nums1) and (temp[1]+1,temp[2]) not in seen:
                seen.add((temp[1]+1,temp[2]))
                heapq.heappush(li,
                (nums1[temp[1]+1]+nums2[temp[2]],temp[1]+1,temp[2])
                )
        return ans

'''
refer

https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/solution/bu-chong-guan-fang-ti-jie-you-xian-dui-l-htf8/
'''



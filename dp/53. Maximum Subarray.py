class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[]
        pre=0
        for e in nums:
            if pre>0:
                arr.append(pre+e)
                pre=pre+e
            else:
                arr.append(e)
                pre=e
        return max(arr)
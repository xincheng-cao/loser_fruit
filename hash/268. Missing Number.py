class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(nums)
        i=0
        right=len(nums)
        for i in range(0,right+1):
            if i not in s:
                return i
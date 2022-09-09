class Solution:
    def multiple(self,nums):
        ans=1
        for i in nums:
            ans*=i
        return ans
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]==0:
                ans_list=[0]*len(nums)
                nums[i]=1
                ans_list[i]=self.multiple(nums)
                return ans_list
        prod=self.multiple(nums)
        ans_list=[]
        for i in range(len(nums)):
            ans_list.append(int(prod/nums[i]))
        return ans_list

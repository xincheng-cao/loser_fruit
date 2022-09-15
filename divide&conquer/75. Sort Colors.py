class Solution:
    def swap(self, a, b, nums):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # loop in variant
        # if len(nums)<=1:
        #    return

        # head and tail node !!
        nums.insert(0, 0)
        nums.append(2)
        left = 0
        right = len(nums) - 1
        i = 1
        while left < right and i > left and i < right:
            if nums[i] == 0:
                self.swap(i, left + 1, nums)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1

            else:  # ==2
                self.swap(i, right - 1, nums)
                right -= 1
        nums.pop()
        nums.pop(0)


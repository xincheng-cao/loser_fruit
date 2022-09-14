class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) <= 2:
            return ans

        nums.sort()

        for i in range(len(nums)):
            if i > 0:
                # briliant
                if (nums[i - 1] == nums[i]):
                    continue

            if nums[i] > 0:
                continue

            if i + 2 >= len(nums):
                break

            left = i + 1
            right = len(nums) - 1
            while left < right and left < len(nums) and right < len(nums) and left >= 0 and right >= 0:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    '''
                    # cant simply do this because [-3,1,1,2,2]
                    left+=1
                    right-=1
                    '''
                    temp_left = nums[left]
                    temp_right = nums[right]
                    while nums[left] == temp_left:
                        left += 1
                        if left >= len(nums):
                            break
                    while nums[right] == temp_right:
                        right -= 1
                        if right < 0: break
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1

        return ans
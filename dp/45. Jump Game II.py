class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        i = 0

        while i < len(nums):

            temp = [k for k in range(i + 1, i + nums[i] + 1)]
            if temp[-1] >= len(nums) - 1:
                ans += 1
                break
            next_idx = temp[0]
            longest = next_idx + nums[next_idx]
            for j in range(1, len(temp)):
                temp_idx = temp[j]
                temp_longest = temp_idx + nums[temp_idx]
                if temp_longest > longest:
                    longest = temp_longest
                    next_idx = temp_idx
            i = next_idx
            ans += 1
        return ans








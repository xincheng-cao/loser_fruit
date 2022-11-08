class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [0] * len(nums)
        dp_c = [0] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                dp[i] = 1
                dp_c[i] = 1
                continue
            max_len = 1
            max_c = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    temp_len = dp[j] + 1
                    if temp_len > max_len:
                        max_len = temp_len
                        max_c = dp_c[j]
                    elif temp_len == max_len:
                        max_c += dp_c[j]
            dp[i] = max_len
            dp_c[i] = max_c
        max_len = max(dp)
        res = 0
        for i in range(len(dp)):
            if dp[i] == max_len:
                res += dp_c[i]
        return res

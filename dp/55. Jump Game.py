class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        cur_idx = 0

        while cur_idx < len(nums):
            if nums[cur_idx] == 0 and cur_idx != len(nums) - 1:
                return False
            cand_idx = [
                k for k in range(cur_idx + 1, cur_idx + nums[cur_idx] + 1)
            ]

            # if cand_idx[-1]>=len(nums)-1:return True

            next_step_idx = cand_idx[0]
            if next_step_idx >= len(nums) - 1: return True
            longest = next_step_idx + nums[next_step_idx]
            for i in range(1, len(cand_idx)):
                temp_step_idx = cand_idx[i]
                if temp_step_idx >= len(nums) - 1: return True
                if longest < temp_step_idx + nums[temp_step_idx]:
                    next_step_idx = temp_step_idx
                    longest = temp_step_idx + nums[temp_step_idx]
            cur_idx = next_step_idx



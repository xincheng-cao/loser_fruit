class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        target_set = set()

        i = 0
        while (i < len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp_target = nums[i] + nums[left] + nums[right]
                if temp_target == target:
                    return target
                elif temp_target > target:
                    right -= 1
                    target_set.add(temp_target)
                else:
                    left += 1
                    target_set.add(temp_target)
            i += 1
        target_set = list(target_set)

        min_diff = pow(2, 32) - 1
        best_target = None
        for e in target_set:
            if abs(e - target) < min_diff:
                min_diff = abs(e - target)
                best_target = e
        return best_target
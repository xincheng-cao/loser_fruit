class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # return self.selection_sort(nums)
        return self.quick_sort(nums)

    def _quick_sort(self, nums, start_idx, end_idx):
        if start_idx >= end_idx:
            return
        std_idx = self._partition(nums, start_idx, end_idx)
        self._quick_sort(nums, start_idx, std_idx - 1)
        self._quick_sort(nums, std_idx + 1, end_idx)

    def _partition(self, nums, start_idx, end_idx):
        std_idx = start_idx
        left_part_end_idx = start_idx
        for right_part_start_idx in range(start_idx + 1, end_idx + 1):
            if str(nums[right_part_start_idx]) + str(nums[std_idx]) > str(nums[std_idx]) + str(
                    nums[right_part_start_idx]):
                left_part_end_idx += 1
                nums[right_part_start_idx], nums[left_part_end_idx] = nums[left_part_end_idx], nums[
                    right_part_start_idx]
        nums[std_idx], nums[left_part_end_idx] = nums[left_part_end_idx], nums[std_idx]
        return left_part_end_idx

    def quick_sort(self, nums: List[int]):
        self._quick_sort(nums, 0, len(nums) - 1)
        ans = ''
        if nums[0] == 0: return '0'
        for e in nums:
            ans += str(e)
        return ans

    def selection_sort(self, nums: List[int]):
        for i in range(len(nums)):
            max_idx = i
            for j in range(i + 1, len(nums)):

                if str(nums[max_idx]) + str(nums[j]) < str(nums[j]) + str(nums[max_idx]):
                    max_idx = j

            temp = nums[i]
            nums[i] = nums[max_idx]
            nums[max_idx] = temp
        ans = ''
        for e in nums:
            ans += str(e)
        if nums[0] == 0: return '0'
        return ans
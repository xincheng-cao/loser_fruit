class Solution:
    def three_way_quick_sel(self, nums):
        def partition(nums, start_idx, end_idx):
            std_val = nums[start_idx]
            # left_part_end_idx is not -1!!!
            left_part_end_idx = start_idx - 1
            # right_part_start_idx is not len(nums)!!!
            right_part_start_idx = end_idx + 1

            i = start_idx
            while i < right_part_start_idx:
                if nums[i] < std_val:
                    left_part_end_idx += 1
                    nums[i], nums[left_part_end_idx] = \
                        nums[left_part_end_idx], nums[i]
                    i += 1
                elif nums[i] > std_val:
                    right_part_start_idx -= 1
                    nums[i], nums[right_part_start_idx] = \
                        nums[right_part_start_idx], nums[i]
                else:
                    i += 1
            return left_part_end_idx, right_part_start_idx

        expected_mid_idx = (len(nums) - 1) // 2
        start_idx = 0
        end_idx = len(nums) - 1
        left_part_end_idx, right_part_start_idx = \
            partition(nums, start_idx, end_idx, )
        while not (left_part_end_idx < expected_mid_idx and right_part_start_idx > expected_mid_idx):
            if right_part_start_idx <= expected_mid_idx:
                start_idx = right_part_start_idx
            else:  # left_part_end_idx>=expected_mid_idx
                end_idx = left_part_end_idx
            if start_idx > end_idx: raise Exception('sss')
            left_part_end_idx, right_part_start_idx = \
                partition(nums, start_idx, end_idx)

        tgt_mid = expected_mid_idx
        print(nums)
        left_part = nums[:tgt_mid + 1]
        right_part = nums[tgt_mid + 1:]
        print(left_part, right_part)
        right_part.reverse()
        left_part.reverse()
        for i in range(len(right_part)):
            nums[i * 2] = left_part[i]
            nums[i * 2 + 1] = right_part[i]
        if len(left_part) > len(right_part):
            nums[-1] = left_part[-1]
        return

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # way1
        self.three_way_quick_sel(nums)
        return

        # way2
        def partition(nums, start_idx, end_idx):
            std_idx = start_idx
            left_part_end_idx = start_idx

            for right_part_start_idx in range(start_idx + 1, end_idx + 1):
                if nums[right_part_start_idx] < nums[std_idx]:
                    left_part_end_idx += 1
                    nums[left_part_end_idx], nums[right_part_start_idx] = \
                        nums[right_part_start_idx], nums[left_part_end_idx]
            nums[std_idx], nums[left_part_end_idx] = \
                nums[left_part_end_idx], nums[std_idx]
            return left_part_end_idx

        left = 0
        right = len(nums) - 1
        tgt_mid = (len(nums) - 1) // 2
        cur_mid = partition(nums, left, right)
        while not tgt_mid == cur_mid:
            if cur_mid > tgt_mid:
                right = cur_mid - 1  # cur_mid wont be median so declude it

            else:
                left = cur_mid + 1
            cur_mid = partition(nums, left, right)

        median_val = nums[tgt_mid]
        print(nums)

        # he lan qi / 3 way partition -> let all the mid val in the mid!!
        # dont care left/right part is sorted or not
        left_part_end_idx = -1
        right_part_start_idx = len(nums)
        i = 0
        while i < right_part_start_idx:
            if nums[i] < median_val:
                left_part_end_idx += 1
                nums[i], nums[left_part_end_idx] = nums[left_part_end_idx], nums[i]
                # 换走的这个left_part_end_idx 对应的值要一定<=median_val
                # 所以i可以放心++
                i += 1
            elif nums[i] > median_val:
                right_part_start_idx -= 1
                nums[i], nums[right_part_start_idx] = nums[right_part_start_idx], nums[i]
                # 换回来的这个right_part_start_idx 的值不一定是median_val
                # 所以i不能++ 所以等于原地不动
            else:
                i += 1

        print(nums)
        left_part = nums[:tgt_mid + 1]
        right_part = nums[tgt_mid + 1:]
        print(left_part, right_part)
        right_part.reverse()
        left_part.reverse()
        for i in range(len(right_part)):
            nums[i * 2] = left_part[i]
            nums[i * 2 + 1] = right_part[i]
        if len(left_part) > len(right_part):
            nums[-1] = left_part[-1]
        return
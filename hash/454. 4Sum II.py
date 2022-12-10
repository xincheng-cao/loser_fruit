class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        left_d = dict()
        right_d = dict()
        ans = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums2[j] + nums1[i]
                if sum in left_d:
                    left_d[sum] += 1
                else:
                    left_d[sum] = 1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums3[j] + nums4[i]
                if sum in right_d:
                    right_d[sum] += 1
                else:
                    right_d[sum] = 1

        for left in left_d.keys():
            if left * (-1) in right_d:
                ans += left_d[left] * right_d[-1 * left]
        return ans
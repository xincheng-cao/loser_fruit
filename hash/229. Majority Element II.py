class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element2count = dict()

        for e in nums:
            if e in element2count:
                element2count[e] += 1
            else:
                element2count[e] = 1

        ans = []
        for k, v in element2count.items():
            if v > len(nums) / 3:
                ans.append(k)
        return ans
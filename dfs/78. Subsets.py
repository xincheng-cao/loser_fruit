class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(prev, idx):
            for i in range(idx + 1, len(nums)):
                temp = list(prev + [nums[i]])
                res.append(temp)
                dfs(temp, i)

        dfs([], -1)
        return [[]] + res
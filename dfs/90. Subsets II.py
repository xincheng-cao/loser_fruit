class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort 1
        nums.sort()

        res = []

        def dfs(prev, idx):
            prev_item = -99999
            for i in range(idx + 1, len(nums)):

                # prune 2
                if nums[i] == prev_item:
                    continue
                else:
                    prev_item = nums[i]

                temp = list(prev + [nums[i]])
                res.append(temp)
                dfs(temp, i)

        dfs([], -1)
        res = [[]] + res
        return res
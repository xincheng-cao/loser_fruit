class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            k = nums[i]
            v = i
            if k in map:
                map[k].append(v)
            else:
                map[k] = [v]

        for i in range(len(nums)):
            k = nums[i]
            v = i
            rem = target - k
            if rem == k:
                if map[rem].__len__() == 2:
                    return map[k]
                else:
                    continue
            else:
                if rem in map:
                    return [map[k][0], map[rem][0]]
                else:
                    continue
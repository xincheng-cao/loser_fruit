class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix_sun = []
        sum = 0
        for e in nums:
            sum += e
            self._prefix_sun.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sun[right]

        res = self._prefix_sun[right] - self._prefix_sun[left - 1]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
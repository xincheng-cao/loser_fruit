class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        '''

        最后写出的代码和题解类似，讲下我的思考过程。 首先对数组排序，然后最重要的一个思想是，排序后的数组中，一定有一个位置 i，i 本身及左测全部加 K,i 右侧全部减 K。 即A[0]..A[i]全部加上K，A[i+1]..A[n-1]全部减去 K， 此时整个数组的最大值是 A[n-1]-K 或 A[i]+K，最小值是 A[0]+K 或 A[i+1]-K。 有了这个前提后，就可以线性扫描 i从0到 n-2(i 等于 n-1相当于全部加 K，也就是原始的最大值-最小值)，求出最小的可能值。
        for every position i use the method above can get a local optimal(greedy)
        but if consider all the i convert local optimal -> global optimal
        '''

        nums.sort()
        optimal = max(nums) - min(nums)  # optimal = float('inf') #this is wrong!

        if len(nums) == 1:
            return 0

        for i in range(1, len(nums)):
            left = nums[:i]
            right = nums[i:]

            maxx = max(left[-1] + k, right[-1] - k)
            minn = min(left[0] + k, right[0] - k)

            if maxx - minn < optimal:
                optimal = maxx - minn
        return optimal

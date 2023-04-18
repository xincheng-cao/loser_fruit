class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1.将各区间根据右边界大小排列
        2.遍历所有区间，如果当前区间的左边界与上一区的右边界重叠，说明需要移除某一个区间
        3.贪心，在两个重合区间中，保留右边界较小的那一个区间，这样可以尽可能减少与下一个区间重合的可能性
        **** draw a pic and you will understand
1.
|---|
 |--|x
or
|---|
|---|x
or
 |--|
|---|x
2.
  |---|
|-------|x
3.
|---|
  |---|x
4. ok
|---|
    |---|
        '''
        ans = 0

        def get_elm(li):
            return li[-1]

        intervals.sort(key=get_elm, reverse=False)

        i = 0
        while i < len(intervals) - 1:
            left = intervals[i]
            right = intervals[i + 1]

            if left[-1] > right[0]:
                # intervals.pop(i+1)
                intervals[i + 1] = intervals[i]
                i += 1
                ans += 1
            else:
                i += 1
        return ans


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1: return 0

        def is_sorted(res_list):
            left = 0
            right = 1
            flag = True
            while right < len(res_list):
                if res_list[left] <= res_list[right]:
                    left += 1
                    right += 1
                else:
                    flag = False
                    break

            return flag

        res_list = [''] * len(strs)
        ans = 0
        for col in range(len(strs[0])):
            for row in range(len(strs)):
                res_list[row] += strs[row][col]
            if not is_sorted(res_list):
                for row in range(len(strs)):
                    res_list[row] = res_list[row][:-1]
                ans += 1
        return ans
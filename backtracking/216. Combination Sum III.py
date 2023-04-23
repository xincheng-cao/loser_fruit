class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        cur_sel_list = []

        def dfs(remainder: int):
            tb_sel_len = k - len(cur_sel_list)
            cur_sel = cur_sel_list[-1]

            if tb_sel_len == 0:
                if remainder == cur_sel:
                    ans.append([t for t in cur_sel_list])
                else:
                    pass
            else:
                if remainder < cur_sel:
                    pass
                elif cur_sel - tb_sel_len <= 0:
                    pass
                elif remainder > (cur_sel + cur_sel - tb_sel_len) * (tb_sel_len + 1) / 2:
                    pass
                else:
                    remainder = remainder - cur_sel
                    for next_sel in range(cur_sel - 1, 0, -1):
                        cur_sel_list.append(next_sel)
                        # print(cur_sel_list)
                        dfs(remainder)
                        cur_sel_list.pop()

        for next_sel in range(9, 0, -1):
            cur_sel_list.append(next_sel)
            dfs(n)
            cur_sel_list.pop()
        return ans



















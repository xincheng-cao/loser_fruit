class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(res, cur, ):
            if len(cur) == k:
                res.append(cur)
            if len(cur) > 0:
                last = cur[-1]
            else:
                last = 0
            if last >= n:
                return
            else:
                for i in range(last + 1, n + 1):
                    dfs(res, list(cur + [i]))

        dfs(res, [])
        return res


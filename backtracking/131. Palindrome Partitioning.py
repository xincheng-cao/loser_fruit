class Solution:
    def partition(self, s: str):
        arr = []
        for i in range(len(s)):
            arr.append([0] * len(s))

        for i in range(len(s)):
            arr[i][i] = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                arr[i][i + 1] = 1

        for i in range(2, len(s)):
            left = 0
            right = i
            while right < len(s):
                if arr[left + 1][right - 1] == 1:
                    if s[left] == s[right]:
                        arr[left][right] = 1
                left += 1
                right += 1

        level = dict()
        for i in range(len(s)):
            level[i] = []
            for j in range(i, len(s)):
                if arr[i][j] == 1:
                    level[i].append((i, j))

        def dfs(start: int):
            res = []
            if start >= len(s):
                return []
            for e in level[start]:
                if e[1] == len(s) - 1:
                    res.append([s[e[0]:e[1]+1]])
                else:
                    temp = dfs(e[1] + 1)
                    for tt in temp:
                        tt.insert(0, s[e[0]:e[1]+1])
                    res += temp
            return res

        return dfs(0)



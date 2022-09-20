class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ''
        left = 0
        right = 0
        res_list = []

        self.dfs(s, left, right, n, res_list)
        return res_list

    def dfs(self, s, left, right, n, res_list):
        if right > left:
            return
        if left > n:  # easy to forget
            return
        if right + left == n * 2:
            res_list.append(s)

        s1 = s + '('
        left1 = left + 1
        right1 = right
        self.dfs(s1, left1, right1, n, res_list)

        s2 = s + ')'
        left2 = left
        right2 = right + 1
        self.dfs(s2, left2, right2, n, res_list)


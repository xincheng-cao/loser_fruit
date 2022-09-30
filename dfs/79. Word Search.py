class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(s, i, j, word):

            if len(word) == 0:
                return True
            if board[i][j] != word[0]:
                return False
            s.add(str(i) + str(j))
            temp_word = word[1:]
            if temp_word.__len__() == 0:
                return True
            for d in dir:
                i_1 = i + d[0]
                j_1 = j + d[1]
                if i_1 < 0 or i_1 >= len(board) or j_1 < 0 or j_1 >= len(board[0]):
                    continue
                if str(i_1) + str(j_1) in s:
                    continue
                if board[i_1][j_1] != temp_word[0]:
                    continue

                if dfs(s, i_1, j_1, temp_word):
                    return True
            s.remove(str(i) + str(j))
            return False

        for u in range(len(board)):
            for v in range(len(board[0])):
                s = set()
                if dfs(s, u, v, word):
                    return True
        return False


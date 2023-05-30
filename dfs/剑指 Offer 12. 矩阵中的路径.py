import copy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 1:
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] == word[0]:
                        return True
            return False

        visited = copy.deepcopy(board)

        def dfs(word_idx: int, cur_board_row: int, cur_board_col: int, ):
            for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if cur_board_row + delta_x < 0 or cur_board_row + delta_x >= len(board):
                    continue
                if cur_board_col + delta_y < 0 or cur_board_col + delta_y >= len(board[0]):
                    continue
                x = cur_board_row + delta_x
                y = cur_board_col + delta_y
                if visited[x][y] == 'visited':
                    continue
                if word[word_idx] == board[x][y]:
                    if word_idx == len(word) - 1:
                        return True
                    else:
                        visited[x][y] = 'visited'
                        if dfs(word_idx + 1, x, y, ):
                            visited[x][y] = 'unvisited'
                            return True
                        visited[x][y] = 'unvisited'
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    visited[x][y] = 'visited'
                    if dfs(1, x, y):
                        return True
                    visited[x][y] = 'unvisited'
        return False


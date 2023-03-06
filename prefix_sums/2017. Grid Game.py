class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        i = 0
        below = grid[1][:i]
        up = grid[0][i + 1:]
        sum_up = 0
        sum_below = 0
        for e in below:
            sum_below += e
        for e in up:
            sum_up += e
        ans = max(sum_up, sum_below)

        for i in range(1, len(grid[0])):
            sum_below += grid[1][i - 1]

            sum_up -= grid[0][i]

            if max(sum_up, sum_below) < ans:
                ans = max(sum_up, sum_below)
        return ans
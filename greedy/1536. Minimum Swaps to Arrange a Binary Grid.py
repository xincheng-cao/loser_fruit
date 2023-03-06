class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        li = []
        ans = 0

        for row in range(n):
            count = 0
            for col in range(n):
                if grid[row][n - 1 - col] == 0:
                    count += 1
                else:
                    break
            li.append(n - count)
        # print(li)

        for i in range(n):
            if li[i] <= i + 1:
                continue
            right = -1
            for j in range(i + 1, n):
                if li[j] <= i + 1:
                    right = j
                    break

            if right == -1:
                return -1

            # linked list pop / insert time complexity o(1)
            # bubble time complexity o(n)
            temp = li.pop(right)
            li.insert(i, temp)
            # print(li)
            ans += (right - i)
        return ans


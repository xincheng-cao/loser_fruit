from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.root = []
        for i in range(n):
            self.root.append(i)
        self.size = [1] * n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.size[root_x] = 0
        self.part -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        part = defaultdict(list)
        for i in range(len(self.root)):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        size = defaultdict(int)
        for i in range(len(self.root)):
            size[self.find(i)] = self.size[self.find(i)]
        return size


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        if rows == 1 or cols == 1: return False

        pos2mem = dict()
        for r in range(rows):
            for c in range(cols):
                pos2mem[(r, c)] = cols * r + c

        uf = UnionFind(n=rows * cols)

        for r in range(rows):
            for c in range(cols - 1):
                if grid[r][c] == grid[r][c + 1]:
                    left = pos2mem[(r, c)]
                    right = pos2mem[r, c + 1]
                    if uf.is_connected(left, right):
                        return True
                    else:
                        uf.union(left, right)

        for r in range(rows - 1):
            for c in range(cols):
                if grid[r][c] == grid[r + 1][c]:
                    top = pos2mem[(r, c)]
                    down = pos2mem[(r + 1, c)]
                    if uf.is_connected(top, down):
                        return True
                    else:
                        uf.union(top, down)

        return False

























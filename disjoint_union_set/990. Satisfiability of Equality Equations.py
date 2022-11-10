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
    def equationsPossible(self, equations: List[str]) -> bool:
        param_dict = dict()
        idx = 0
        for e in equations:
            left = e[0]
            right = e[-1]
            if left not in param_dict:
                param_dict[left] = idx
                idx += 1
            if right not in param_dict:
                param_dict[right] = idx
                idx += 1

        uf = UnionFind(len(param_dict))
        saved = []
        for e in equations:
            left = e[0]
            right = e[-1]
            if e[1] == '=':
                uf.union(param_dict[left], param_dict[right])
            else:
                saved.append((left, right))
        for t in saved:
            if uf.is_connected(param_dict[t[0]], param_dict[t[1]]):
                return False
        return True

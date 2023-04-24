from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Return AN edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs LAST in the input.
        '''

        # n == edges.length
        n = len(edges)

        uf = UnionFind(n=n)

        # n>=3
        uf.union(edges[0][0] - 1, edges[0][1] - 1)
        ans_idx = 0

        for i in range(1, n):
            # print(i,uf.is_connected(edges[i][0]-1,edges[i][1]-1))
            if uf.is_connected(edges[i][0] - 1, edges[i][1] - 1):
                ans_idx = i
            else:
                # ans_idx=i
                uf.union(edges[i][0] - 1, edges[i][1] - 1)
        return edges[ans_idx]


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













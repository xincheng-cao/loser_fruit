from collections import defaultdict, Counter


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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        uf = UnionFind(len(source))

        for swap in allowedSwaps:
            uf.union(swap[0], swap[1])

        connected_components = uf.get_root_part()
        res = 0

        for cc_k, cc in connected_components.items():
            # cc can be like {1,2,3,0,4} and {5}
            # {5} is not allowed swap
            temp_source = [source[idx] for idx in cc]
            temp_tartget = [target[idx] for idx in cc]

            temp_source_counter = Counter(temp_source)
            temp_tartget_counter = Counter(temp_tartget)

            for k in temp_source_counter:  # duplicate values in source and target
                if not k in temp_tartget_counter:
                    res += temp_source_counter[k]
                else:
                    if temp_source_counter[k] > temp_tartget_counter[k]:
                        res += (temp_source_counter[k] - temp_tartget_counter[k])

        return res


























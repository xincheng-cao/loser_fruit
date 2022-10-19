from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.root=[]
        for i in range(n):
            self.root.append(i)
        self.size=[1]*n
        self.part=n

    def find(self,x):
        if x!=self.root[x]:
            root_x=self.find(self.root[x])
            self.root[x]=root_x
            return root_x
        return x

    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x==root_y:
            return

        if self.size[root_x]>=self.size[root_y]:
            root_x,root_y=root_y,root_x
        self.root[root_x]=root_y
        self.size[root_y]+=self.size[root_x]
        self.size[root_x]=0
        self.part-=1

    def is_connected(self,x,y):
        return self.find(x)==self.find(y)

    def get_root_part(self):
        part=defaultdict(list)
        for i in range(len(self.root)):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        size=defaultdict(int)
        for i in range(len(self.root)):
            size[self.find(i)]=self.size[self.find(i)]
        return size

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf=UnionFind(len(graph))
        for i in range(len(graph)):
            for j in range(0,len(graph[i])):
                uf.union(graph[i][0],graph[i][j])
                if uf.is_connected(graph[i][j],i):
                    return False
        return True

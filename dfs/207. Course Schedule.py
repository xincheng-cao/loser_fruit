class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(idx: int):
            if node_color[idx] == 1:
                return False
            if node_color[idx] == -1:
                return True
            ##==0
            if idx not in graph:
                node_color[idx] = -1
                return True
            else:
                node_color[idx] = 1
                for next in graph[idx]:
                    if not dfs(next):
                        return False
                node_color[idx] = -1  # easy to forget
                return True

        graph = dict()
        for e in prerequisites:
            if e[0] in graph:
                graph[e[0]].append(e[1])
            else:
                graph[e[0]] = [e[1]]
        node_color = dict()
        for i in range(numCourses):
            node_color[i] = 0

        for i in range(numCourses):
            if i not in graph:
                node_color[i] = -1
                continue
            else:
                if not dfs(i):
                    return False
        return True


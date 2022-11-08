class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        node_colors = [0] * len(graph)
        res = []

        def dfs(node_idx: int):
            out_node_list = graph[node_idx]
            temp_res = True
            if out_node_list.__len__() == 0:
                node_colors[node_idx] = 2
                res.append(node_idx)
                return 2

            node_colors[node_idx] = 1  # color 1 anyway bc it will never be 2
            for n in out_node_list:
                if node_colors[n] == 1:
                    # node_colors[node_idx]=1
                    temp_res = False
                    break
                elif node_colors[n] == 2:
                    continue
                else:  # ==0

                    if dfs(n) == 1:
                        # node_colors[node_idx]=1
                        temp_res = False
                        break
                    else:  ##==2
                        continue
            if temp_res:
                res.append(node_idx)
                node_colors[node_idx] = 2
                return 2  # easy to forget
            else:
                return 1

        for i in range(len(graph)):
            if node_colors[i] == 0:
                dfs(i)
        res.sort()
        return res

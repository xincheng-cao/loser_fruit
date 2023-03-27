class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        stack=[]

        def dfs(start_node):
            if start_node==len(graph)-1:
                stack.append(start_node)
                ans.append(stack[:])
                #stack.clear()
            else:
                stack.append(start_node)
                for n in graph[start_node]:
                    dfs(n)
                    stack.pop()

        dfs(0)

        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        # from functools import lru_cache
        # @lru_cache(maxsize=None)
        def dfs(start: int, end: int) -> List:
            if start > end: return []
            # if start==end: return [TreeNode(start)]
            ans = []
            for i in range(start, end + 1):

                temp_left = dfs(start, i - 1)
                temp_right = dfs(i + 1, end)
                if len(temp_left) > 0 and len(temp_right) > 0:
                    for temp_l in temp_left:
                        for temp_r in temp_right:
                            head = TreeNode(i)
                            head.left = temp_l
                            head.right = temp_r
                            ans.append(head)
                elif len(temp_left) > 0:
                    for temp_l in temp_left:
                        temp_r = None
                        head = TreeNode(i)
                        head.left = temp_l
                        head.right = temp_r
                        ans.append(head)
                elif len(temp_right) > 0:
                    for temp_r in temp_right:
                        temp_l = None
                        head = TreeNode(i)
                        head.left = temp_l
                        head.right = temp_r
                        ans.append(head)
                elif len(temp_left) == 0 and len(temp_right) == 0:
                    head = TreeNode(i)
                    temp_r = None
                    temp_l = None
                    head.left = temp_l
                    head.right = temp_r
                    ans.append(head)

            return ans

        return dfs(1, n)






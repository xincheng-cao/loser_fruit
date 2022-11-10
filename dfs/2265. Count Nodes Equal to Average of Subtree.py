# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: TreeNode):
            nonlocal res

            if node is None:
                return None, 0
            sum = node.val
            num = 1
            temp_res = dfs(node.left)
            if temp_res[0] is None:
                pass
            else:
                sum += temp_res[0]
                num += temp_res[1]

            temp_res = dfs(node.right)
            if temp_res[0] is None:
                pass
            else:
                sum += temp_res[0]
                num += temp_res[1]
            if int(sum / num) == node.val:
                res += 1
            return sum, num

        dfs(root)
        return res

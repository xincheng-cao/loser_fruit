# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        leftmostheight = 0
        leftmostval = root.val

        def dfs(node: TreeNode, cur_height: int):
            ### important!!!
            nonlocal leftmostval, leftmostheight
            ###
            if node is None:
                return
            if node.left is not None:
                if cur_height + 1 > leftmostheight:
                    leftmostval = node.left.val
                    leftmostheight = cur_height + 1
                dfs(node.left, cur_height + 1)
            if node.right is not None:
                ### important!!!
                if node.left is None:
                    if cur_height + 1 > leftmostheight:
                        leftmostval = node.right.val
                        leftmostheight = cur_height + 1
                ###
                dfs(node.right, cur_height + 1)

        dfs(root, 0)
        return leftmostval

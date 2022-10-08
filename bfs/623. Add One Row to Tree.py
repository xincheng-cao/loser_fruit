# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # depth >=1
        if depth == 1:
            return TreeNode(val, root, None)  # default go left

        q = [root]
        for i in range(depth - 2):
            q2 = []
            while len(q) > 0:
                temp = q.pop()
                if temp.left is not None:  # important otherwise None is appended
                    q2.append(temp.left)
                if temp.right is not None:
                    q2.append(temp.right)
            q = q2
        # return q
        for i in q:
            # if i.left is not None: # well if it dont have child it can still add a layer below
            i.left = TreeNode(val, i.left, None)
            # if i.right is not None:
            i.right = TreeNode(val, None, i.right)
        return root

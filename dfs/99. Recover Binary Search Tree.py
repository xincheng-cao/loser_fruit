# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
         where the values of exactly two nodes of!!
        '''
        vec = []

        def dfs(root):
            if root.left is not None:
                dfs(root.left)
            vec.append(root.val)
            if root.right is not None:
                dfs(root.right)

        dfs(root)
        reverse = []
        for i in range(len(vec) - 1):
            if vec[i] > vec[i + 1]:
                reverse.append(i)
                reverse.append(i + 1)

        need_swap = []
        if len(reverse) == 2:
            need_swap.append(vec[reverse[0]])
            need_swap.append(vec[reverse[1]])
        else:  # ==4
            need_swap.append(vec[reverse[0]])
            need_swap.append(vec[reverse[3]])

        # print(reverse,need_swap)

        def dfs2(root):
            # print(root.val)
            if root.val == need_swap[0]:
                root.val = need_swap[1]
            elif root.val == need_swap[1]:
                root.val = need_swap[0]
            # print(root.val)
            if root.left is not None:
                dfs2(root.left)
            if root.right is not None:
                dfs2(root.right)

        dfs2(root)


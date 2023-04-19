# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root:TreeNode)-> list:
            if root is None: return []
            if root.left is None and root.right is None:
                return [str(root.val)]
            ans=[]
            if root.left is not None:
                temp_list= dfs(root.left)
                for temp in temp_list:
                    ans.append(
                        str(root.val)+temp
                    )
            if root.right is not None:
                temp_list=dfs(root.right)
                for temp in temp_list:
                    ans.append(
                        str(root.val)+temp
                    )
            return ans

        ans = dfs(root)
        real_ans=0
        for a in ans:
            real_ans+=int(a)
        return real_ans






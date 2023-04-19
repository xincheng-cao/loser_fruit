# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, prev_sum) -> list:
            if root is None:
                return []
            if root.left is None and root.right is None:
                if prev_sum + root.val == targetSum:
                    return [[root.val]]
            ans = []
            if root.left is not None:
                # if prev_sum+root.val <targetSum:
                templist = dfs(root.left, prev_sum + root.val)
                for temp in templist:
                    temp = [root.val] + temp
                    ans.append(temp)
            if root.right is not None:
                # if prev_sum+root.val<targetSum:
                templist = dfs(root.right, prev_sum + root.val)
                for temp in templist:
                    temp = [root.val] + temp
                    ans.append(temp)
            return ans

        return dfs(root, 0)









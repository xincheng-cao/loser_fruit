# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_list = []

        def dfs(node):
            if node.left is not None:
                dfs(node.left)
            sorted_list.append(node.val)
            if node.right is not None:
                dfs(node.right)

        dfs(root)

        def search(val):
            left = 0
            right = len(sorted_list) - 1
            min_val = sorted_list[0]
            max_val = sorted_list[-1]

            if val < min_val:
                return [-1, min_val]
            if val > max_val:
                return [max_val, -1]

            while (left < right):
                mid = (left + right) // 2
                if sorted_list[mid] == val:
                    return [val, val]
                elif sorted_list[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
            if val == sorted_list[left]:
                return [val, val]
            elif val > sorted_list[left]:
                return [sorted_list[left], sorted_list[left + 1]]
            else:
                return [sorted_list[left - 1], sorted_list[left]]

        res = []
        for e in queries:
            res.append(search(e))
        return res



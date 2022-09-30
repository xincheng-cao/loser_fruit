# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def dfs(s):

            if len(s) == 0:
                return
            if s[0] == '(':  # easy forget
                s = s[1:-1]
            cur = 0
            while cur < len(s):
                if s[cur] == '(':
                    break
                cur += 1
            root = TreeNode(int(s[:cur]), None, None)
            if cur == len(s):
                # left=None
                # right=None
                return root

            stack = []
            curr = cur
            while curr >= cur and curr < len(s):
                if s[curr] == '(':
                    stack.append('(')
                elif s[curr] == ')':
                    stack.pop()
                    if len(stack) == 0:
                        break
                curr += 1
            left = s[cur:curr + 1]

            if curr == len(s):
                right = ''
            else:
                right = s[curr + 1:]

            left = dfs(left)
            right = dfs(right)
            root.left = left
            root.right = right
            return root

        return dfs(s)

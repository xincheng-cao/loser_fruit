# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        que = [root]
        ans = []
        while len(que) > 0:
            temp_ans = []
            new_que = []
            while len(que) > 0:
                node = que.pop()
                temp_ans.append(node.val)
                if node.left is not None:
                    new_que.insert(0, node.left)
                if node.right is not None:
                    new_que.insert(0, node.right)
            ans.append(temp_ans)
            que = new_que

        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][-1::-1]
        return ans

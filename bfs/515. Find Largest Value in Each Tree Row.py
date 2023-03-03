# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=[root]
        res=[]

        while len(queue)>0:
            new_queue=[]
            max_v=-float('inf')
            for e in queue:
                if e.val > max_v:
                    max_v=e.val
                if e.left is not None:
                    new_queue.append(e.left)
                if e.right is not None:
                    new_queue.append(e.right)

            res.append(max_v)
            queue=new_queue
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root, voyage):
        i = -1
        flipped = []

        def dfs(node: TreeNode):
            nonlocal i
            i+=1

            if voyage[i] != node.val: return False

            # All the values in the tree are unique.
            # All the values in voyage are unique.
            # n==node nums==v nums
            if node.left is not None and i + 1 < len(voyage):
                if node.left.val == voyage[i + 1]:
                    if not dfs(node.left):
                        return False
                    else:
                        if node.right is not None:
                            if not dfs(node.right):
                                return False
                            else:
                                return True
                        else:
                            return True

            if node.right is not None and i + 1 < len(voyage):
                if node.right.val == voyage[i + 1]:
                    if not dfs(node.right):
                        return False
                    else:
                        if node.left is not None:
                            if not dfs(node.left):
                                return False
                            else:
                                flipped.append(node.val)
                                return True
                        else:
                            #flipped.append(node.val)
                            #important here!!
                            #doesnt need flip bc preorder travesal doesnt know if ur node is left
                            #or right if you only have one child
                            return True
            if node.left is None and node.right is None:return True
            else:
                return False

        if not dfs(root):
            return [-1]
        else:
            return flipped

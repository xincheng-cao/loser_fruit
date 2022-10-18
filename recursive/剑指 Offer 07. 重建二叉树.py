# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。!!!! go fuck yourself
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # head=None
        index = dict()
        for i in range(len(inorder)):
            index[inorder[i]] = i

        def construct_tree(pre_left, pre_right, in_left, in_right):
            if in_left > in_right or pre_left > pre_right: return None
            if in_left == in_right or pre_left == pre_right: return TreeNode(inorder[in_left])
            mid = TreeNode(preorder[pre_left])
            in_mid_idx = index[preorder[pre_left]]
            if in_mid_idx - 1 >= in_left:
                pre_left_len = in_mid_idx - 1 + 1 - in_left
            else:
                pre_left_len = 0
            if in_right >= in_mid_idx + 1:
                pre_right_len = in_right - (in_mid_idx + 1) + 1
            else:
                pre_right_len = 0

            if pre_left_len > 0:
                mid.left = construct_tree(pre_left + 1, pre_left + pre_left_len, in_left, in_mid_idx - 1)
            else:
                mid.left = None

            if pre_right_len > 0:
                mid.right = construct_tree(pre_left + pre_left_len + 1, pre_left + pre_left_len + pre_right_len,
                                           in_mid_idx + 1, in_right)
            else:
                mid.right = None
            return mid

        return construct_tree(0, preorder.__len__() - 1, 0, preorder.__len__() - 1)













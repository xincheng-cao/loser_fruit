# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
前序遍历为：

(根结点) (前序遍历左分支) (前序遍历右分支)

而后序遍历为：

(后序遍历左分支) (后序遍历右分支) (根结点)
        '''

        def dfs(pre_list, post_list):
            if len(pre_list) == 0: return None

            if len(pre_list) == 1: return TreeNode(pre_list[0], None, None)

            head = TreeNode(pre_list[0], None, None)

            pre_list = pre_list[1:]
            post_list.pop()

            left_set = set()
            right_set = set()

            for i in range(len(pre_list)):
                left_set.add(pre_list[i])
                right_set.add(post_list[i])
                if len(left_set.difference(right_set)) == 0:
                    head.left = dfs(pre_list[:i + 1], post_list[:i + 1])
                    head.right = dfs(pre_list[i + 1:], post_list[i + 1:])
                    return head
                else:
                    pass
            return head

        return dfs(preorder, postorder)

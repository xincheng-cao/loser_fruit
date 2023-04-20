# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None: return 0

        temp_node = root
        heigh = -1
        while temp_node is not None:
            heigh += 1
            temp_node = temp_node.left  # bc complete binary tree
        if heigh == 0: return 1

        # print(heigh)

        left = 0
        right = 2 ** heigh - 1
        always_right_mid = 0
        while (left <= right):
            mid = (left + right) // 2
            if self.node_exist(root, heigh, mid):
                always_right_mid = mid
                left = mid + 1
            else:
                right = mid - 1
        # print(always_right_mid)

        real_ans = always_right_mid + 1
        for i in range(heigh):
            real_ans += pow(2, i)
        return real_ans

    def node_exist(self, root, level, k, ) -> bool:
        '''
        height 2

        level 0                    _
        level 1         0                     1
        level 2     00      01        10            11
        '''
        bin_str = bin(k)[2:]
        max_bin_str = bin(pow(2, level) - 1)[2:]
        bin_str = '0' * (len(max_bin_str) - len(bin_str)) + bin_str
        # print(max_bin_str,bin_str)

        for i in range(len(bin_str)):
            direction = bin_str[i]
            # print(root.val,direction)
            if direction == '0':
                root = root.left
            else:
                root = root.right
            # print(root)
        if root is None:
            return False
        else:
            return True













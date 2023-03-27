# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
    '''

    1 #
    2 ###
      ###
    3
    #######
    #######
    #######
    '''
    def printTree(self,root):

        def cal_h(root,cur_height):
            temp=[]
            if root.left is None and root.right is None:
                return cur_height
            if root.left is not None:
                temp.append(cal_h(root.left,cur_height+1))
            if root.right is not None:
                temp.append(cal_h(root.right,cur_height+1))

            return max(temp)
        rows=cal_h(root,1)
        cols=2**rows-1
        vec=[]
        for r in range(rows):
            vec.append([""]*cols)
        #print(rows,cols)

        def note_tree(root,row,left_i,right_i):
            #print(root.val,row,col)
            col=(left_i+right_i)//2
            vec[row][col]=str(root.val)
            if root.left is not None:
                note_tree(root.left,row+1, left_i,col-1)
            if root.right is not None:
                note_tree(root.right, row + 1, col+1,right_i)
        note_tree(root,0,0,cols)
        return vec
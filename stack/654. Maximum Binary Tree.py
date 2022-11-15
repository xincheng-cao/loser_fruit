# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack=[]
        temp_node=TreeNode(val=nums[0],left=None,right=None)

        stack.append(temp_node)
        idx=1

        while len(stack)>0:
            if idx>=len(nums):
                length=len(stack)-1
                for i in range(length):
                    stack[i].right=stack[i+1]
                return stack[0]
            else:
                temp_node=TreeNode(val=nums[idx],left=None,right=None)
                idx+=1
                #All integers in nums are unique.
                if temp_node.val<stack[-1].val:
                    stack.append(temp_node)
                    continue
                else:
                    if temp_node.val<stack[0].val:
                        # [1,2,3,4,10,7,6,5,8,9] node 8
                        i=1
                        for i in range(1,len(stack)):
                            if stack[i].val<temp_node.val:
                                break
                        # there must be a i , the most case is -1
                        nums_to_pop=len(stack)-i
                        to_pop=stack[i:]
                        stack=stack[:i]
                        cur_node=temp_node
                        for j in range(len(to_pop)):
                            if j==0:
                                cur_node.left=to_pop[j]
                                cur_node=cur_node.left
                            else:
                                cur_node.right=to_pop[j]
                                cur_node=cur_node.right
                        stack.append(temp_node)
                        del i
                    else:
                        # only two scenarios
                        # 1: stack->[0]    0 < temp_node
                        # 2: stack->[0,1,2,...,n]     0>1>2>...>n<temp_node and temp_node>0
                        if len(stack)==1:
                            temp_node.left=stack.pop()
                            stack.append(temp_node)
                            continue
                        else:
                            start=len(stack)-1
                            for i in range(start,0,-1):
                                stack[i-1].right=stack[i]
                                stack.pop()
                            temp_node.left=stack.pop()
                            stack.append(temp_node)
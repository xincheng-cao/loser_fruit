# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        head = None
        cur = None
        ad_flag = 0
        while left is not None or right is not None:
            if left is None:
                left_val = 0
            else:
                left_val = left.val
            if right is None:
                right_val = 0
            else:
                right_val = right.val

            sum = left_val + right_val + ad_flag
            if sum >= 10:
                ad_flag = 1
            else:
                ad_flag = 0
            '''
            temp_node=ListNode(val=sum-10*ad_flag,next=res)
            res=temp_node
            left=left.next
            right=right.next
            '''
            temp_node = ListNode(val=sum - 10 * ad_flag)
            if cur is None:
                head = temp_node
                cur = head
            else:
                cur.next = temp_node
                cur = cur.next
            if left is not None:
                left = left.next
            else:
                left = None

            if right is not None:
                right = right.next
            else:
                right = None

        if ad_flag == 1:
            cur.next = ListNode(1)

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left=ListNode(None,None)
        right= ListNode(None,None)
        left_cur=left
        right_cur=right

        cur = head
        while cur is not None:
            if cur.val<x:
                left_cur.next=cur
                left_cur=left_cur.next
            else:
                right_cur.next=cur
                right_cur=right_cur.next
            cur=cur.next
        left_cur.next=None
        right_cur.next=None
        if left_cur.val is None:
            return right.next
        left_cur.next=right.next
        return left.next
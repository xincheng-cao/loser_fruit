# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        if head.next is None: return head
        if head.next.next is None: return head

        fake_left_head=ListNode(None,None)
        fake_right_head=ListNode(None,None)
        cur_left=fake_left_head
        cur_right=fake_right_head

        cur = head
        flag='left'
        while cur is not None:
            if flag=='left':
                cur_left.next=cur
                cur=cur.next
                cur_left=cur_left.next
                cur_left.next=None
                flag='right'
            else:
                cur_right.next=cur
                cur=cur.next
                cur_right=cur_right.next
                cur_right.next=None
                flag='left'

        cur_left.next=fake_right_head.next
        return fake_left_head.next
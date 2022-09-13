# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        before=None
        if head is None:
            return None


        while cur is not None:
            next=cur.next
            cur.next=before
            before=cur
            cur=next

        return before        
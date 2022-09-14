# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        if head is None:
            return False

        while fast is not None:
            fast = fast.next
            slow = slow.next
            if fast is None:
                return False
            fast = fast.next
            if fast == slow:
                return True

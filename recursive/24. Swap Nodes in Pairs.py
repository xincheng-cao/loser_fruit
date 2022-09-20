# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # can both recursive and iterative
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        left = head
        right = head.next
        remain = head.next.next
        right.next = left
        left.next = self.swapPairs(remain)
        return right
        # n1->n2-> [________]
        # n2->n1-> recursive([_______])

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fake_little = ListNode(None)
        fake_large = ListNode(None)
        cur_little = fake_little
        cur_large = fake_large

        if head is None: return None

        cur = head
        while cur is not None:
            if cur.val < x:
                cur_little.next = cur
                cur_little = cur_little.next
                cur = cur.next
            else:
                cur_large.next = cur
                cur_large = cur
                cur = cur.next

        cur_large.next = None
        cur_little.next = None
        if fake_little.next is None:
            return fake_large.next
        else:
            cur_little.next = fake_large.next
            return fake_little.next

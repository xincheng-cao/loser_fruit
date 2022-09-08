# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2(self, left: ListNode, right: ListNode):
        if left.val < right.val:
            start = left
            left = left.next
        else:
            start = right
            right = right.next
        cur = start
        while left is not None and right is not None:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left is None:
            cur.next = right
        else:
            cur.next = left
        return start

    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head

        cur_step_1 = head
        cur_step_2 = head

        left, right = None, None
        while cur_step_2 is not None and cur_step_1 is not None:
            if cur_step_2.next is None:
                left = head
                right = cur_step_1.next
                cur_step_1.next = None
                break
            elif cur_step_2.next.next is None:
                left = head
                right = cur_step_1.next
                cur_step_1.next = None
                break
            else:
                cur_step_1 = cur_step_1.next
                cur_step_2 = cur_step_2.next.next
        left = self.sortList(head=left)
        right = self.sortList(head=right)
        head = self.merge2(left=left, right=right)
        return head
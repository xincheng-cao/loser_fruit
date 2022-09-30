# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        deleted = set()
        cur = head
        while (cur is not None):
            if cur.val in s:
                deleted.add(cur.val)
            else:
                s.add(cur.val)
            cur = cur.next

        head = ListNode(val=None, next=head)
        cur_slow = head
        cur_fast = head
        while cur_fast.next is not None:
            cur_fast = cur_fast.next
            while cur_fast.val in deleted:
                cur_fast = cur_fast.next
                if cur_fast is None:
                    break
            if cur_fast is None:
                cur_slow.next = None
                break
            cur_slow.next = cur_fast
            cur_slow = cur_slow.next
        return head.next
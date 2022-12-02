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


# next try
class Solution:
    def fast_slow(self,node):
        if node.next is None:
            return node, None
        if node.next.next is None:
            cur_left=node
            cur_right=node.next
            cur_left.next=None
            return cur_left,cur_right

        cur_left=node
        cur_right=node
        while cur_left is not None and cur_right is not None:
            if cur_right.next is not None:
                if cur_right.next.next is not None:
                    cur_right=cur_right.next.next
                    cur_left=cur_left.next
                    continue
            temp=cur_left
            cur_left=cur_left.next
            temp.next=None
            del temp
            return node, cur_left
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:return head

        left,right=self.fast_slow(head)
        ordered_left=self.sortList(left)
        ordered_right=self.sortList(right)
        if ordered_left is None:return ordered_right
        if ordered_right is None: return ordered_left
        # cant both be None
        fake_head=ListNode(None,None)
        cur=fake_head
        while ordered_left is not None and ordered_right is not None:
            if ordered_left.val < ordered_right.val:
                cur.next=ordered_left
                ordered_left=ordered_left.next
                cur=cur.next
                cur.next=None
            else:
                cur.next=ordered_right
                ordered_right=ordered_right.next
                cur=cur.next
                cur.next=None
        if ordered_left is not None:
            cur.next=ordered_left
        else:
            cur.next=ordered_right
        temp=fake_head.next
        fake_head.next=None
        return temp
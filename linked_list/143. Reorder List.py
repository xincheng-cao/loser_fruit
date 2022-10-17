# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left = head
        reverse_head = None
        len = 0
        while left is not None:
            reverse_head = ListNode(left.val, reverse_head)
            len += 1
            left = left.next
        # return reverse_head

        div_res = len // 2
        div_rem = len % 2

        left = head
        right = reverse_head
        new_ls_head = ListNode(None, None)
        new_ls_cur = new_ls_head
        for i in range(div_res):
            # follow 2 lines are import
            # bc left.next=right will mess up everything!!!
            temp_left_next = left.next
            temp_right_next = right.next

            new_ls_cur.next = left
            left.next = right
            new_ls_cur = new_ls_cur.next.next

            left = temp_left_next
            right = temp_right_next
        if div_rem == 1:
            new_ls_cur.next = left
            new_ls_cur = new_ls_cur.next
            new_ls_cur.next = None
        else:
            new_ls_cur.next = None
        return new_ls_head



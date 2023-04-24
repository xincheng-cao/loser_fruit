# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        if len(stack1) == len(stack2):
            pass
        elif len(stack1) > len(stack2):
            for i in range(len(stack1) - len(stack2)):
                stack2 = [0] + stack2
        else:
            for i in range(len(stack2) - len(stack1)):
                stack1 = [0] + stack1
        # print(stack2,stack1)
        temp = stack1.pop() + stack2.pop()
        head = ListNode(temp % 10)
        adv = temp // 10
        while len(stack1) > 0:
            temp = stack1.pop() + stack2.pop() + adv
            new_head = ListNode(temp % 10)
            adv = temp // 10
            new_head.next = head
            head = new_head

        if adv > 0:
            new_head = ListNode(adv, head)
            return new_head
        else:
            return head










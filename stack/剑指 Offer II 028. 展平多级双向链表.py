"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None: return None
        stack = []
        fake_head = Node(val=None, prev=None, next=None, child=None)
        cur_node = fake_head

        stack.append(head)
        while len(stack) > 0:
            temp_node = stack.pop()
            if temp_node.next is not None:
                stack.append(temp_node.next)
            if temp_node.child is not None:
                stack.append(temp_node.child)

            temp_node.next = None
            temp_node.child = None
            temp_node.prev = None
            cur_node.next = temp_node
            temp_node.prev = cur_node
            cur_node = cur_node.next
        # return fake_head.next
        # next child prev pointer shall set None
        # this is Important and easy to forget bc fake_head still linked
        # if prev is not set None
        res = fake_head.next
        res.prev = None
        return res


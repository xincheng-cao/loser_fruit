class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        self.double_linked_list = DoubleLinkedList()
        self.map = dict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            node1 = self.map[key]
            res = node1.val

            self.double_linked_list.delete_node(node1)
            node1 = Node(key=key, val=res, before=None, after=None)
            self.map[key] = node1
            self.double_linked_list.put_a_newly_create_node_to_head(node1)

            return res

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node1 = self.map[key]
            self.double_linked_list.delete_node(node1)
            node1 = Node(key=key, val=value, before=None, after=None)
            self.map[key] = node1
            self.double_linked_list.put_a_newly_create_node_to_head(node1)
        else:
            if self.cur_size < self.capacity:
                self.cur_size += 1
                node1 = Node(key=key, val=value, before=None, after=None)
                self.map[key] = node1
                self.double_linked_list.put_a_newly_create_node_to_head(node1)
            else:
                node1 = Node(key=key, val=value, before=None, after=None)
                self.map[key] = node1
                rmed_key = self.double_linked_list.delete_tail()
                self.map.pop(rmed_key)
                self.double_linked_list.put_a_newly_create_node_to_head(node1)


class Node:
    def __init__(self, key, val, before, after):
        self.key = key
        self.val = val
        self.before = before
        self.after = after


class DoubleLinkedList:
    def __init__(self):
        self.cur_size = 0
        # self.capacity=capacity
        self.head = Node(key=None, val=None, before=None, after=None)
        self.tail = Node(key=None, val=None, before=None, after=None)
        self.head.after = self.tail
        self.tail.before = self.head

    def put_a_newly_create_node_to_head(self, node1: Node):
        '''
        node0=node1.before
        node2=node1.after
        node0.after=node2
        node2.before=node0
        '''

        node0 = self.head
        node2 = self.head.after
        node0.after = node1
        node1.after = node2
        node2.before = node1
        node1.before = node0

        self.cur_size += 1

    def delete_tail(self) -> int:
        if self.cur_size == 0:
            return None
        else:
            node0 = self.tail.before.before
            node1 = self.tail.before
            node2 = self.tail

            key = node1.key

            node0.after = node2
            node2.before = node0
            self.cur_size -= 1

            return key

    def delete_node(self, node1: Node):
        node0 = node1.before
        node2 = node1.after
        node0.after = node2
        node2.before = node0

        self.cur_size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
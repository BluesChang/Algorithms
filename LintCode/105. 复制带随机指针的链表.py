"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        cloned_map = {}
        cloned_head = RandomListNode(head.label)
        cloned_map[head] = cloned_head
        node = head
        cloned_node = cloned_head
        while node is not None:
            cloned_node.random = node.random
            if node.next is not None:
                cloned_node.next = RandomListNode(node.next.label)
                cloned_map[node.next] = cloned_node.next
            else:
                cloned_node.next = None
            node = node.next
            cloned_node = cloned_node.next
        node = cloned_head
        while node is not None:
            if node.random:
                node.random = cloned_map[node.random]
            node = node.next
        return cloned_head

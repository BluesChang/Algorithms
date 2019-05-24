"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        slow_node = head.next
        fast_node = head.next.next
        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None or fast_node.next.next is None:
                return None
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        slow_node = head
        while slow_node != fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next
        return fast_node

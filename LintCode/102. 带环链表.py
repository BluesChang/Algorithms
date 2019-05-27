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
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return False
        fast_node = head.next
        slow_node = head
        while fast_node != slow_node:
            if fast_node.next is None or fast_node.next.next is None:
                return False
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return True

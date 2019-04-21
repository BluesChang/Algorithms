"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """

    def deleteNode(self, node):
        # write your code here
        if not node:
            return
        if node.next is not None:
            next_node = node.next
            node.val = next_node.val
            node.next = next_node.next

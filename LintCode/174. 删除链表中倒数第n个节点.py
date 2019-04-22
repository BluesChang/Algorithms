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
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        if head is None:
            return None
        if n == 0:
            return head
        ahead_node = behind_node = head
        for i in range(n):
            ahead_node = ahead_node.next
        if ahead_node is None:
            return head.next
        while ahead_node.next is not None:
            ahead_node = ahead_node.next
            behind_node = behind_node.next
        behind_node.next = behind_node.next.next
        return head

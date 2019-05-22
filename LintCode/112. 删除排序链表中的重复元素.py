"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        node = head
        while node is not None and node.next is not None:
            if node.val != node.next.val:
                node = node.next
            else:
                node.next = node.next.next
        return head

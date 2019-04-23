"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            merge_head_node = l1
            merge_head_node.next = self.mergeTwoLists(l1.next, l2)
        else:
            merge_head_node = l2
            merge_head_node.next = self.mergeTwoLists(l1, l2.next)
        return merge_head_node

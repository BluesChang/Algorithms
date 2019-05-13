"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        node1, node2 = headA, headB
        len1, len2 = 0, 0
        while node1 is not None:
            node1 = node1.next
            len1 += 1
        while node2 is not None:
            node2 = node2.next
            len2 += 1
        node1, node2 = headA, headB
        while len1 > len2:
            node1 = node1.next
            len1 -= 1
        while len2 > len1:
            node2 = node2.next
            len2 -= 1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1

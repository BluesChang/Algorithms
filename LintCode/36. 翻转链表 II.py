"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        if not head:
            return
        pre_head = ListNode(0, head)
        mth_node_pre = self.find_kth_node(pre_head, m - 1)
        mth_node = mth_node_pre.next
        nth_node = self.find_kth_node(pre_head, n)
        nth_node_next = nth_node.next
        nth_node.next = None
        self.reverse(mth_node)
        mth_node_pre.next = nth_node
        mth_node.next = nth_node_next
        return pre_head.next

    def find_kth_node(self, head, k):
        for i in range(k):
            if not head:
                return
            head = head.next
        return head

    def reverse(self, head):
        new_head = None
        while head is not None:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head

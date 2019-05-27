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
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None
        cur_node = head
        pre_node = None
        while cur_node is not None:
            next_node = cur_node.next
            if next_node is None or cur_node.val != next_node.val:
                pre_node = cur_node
            else:
                while next_node is not None and next_node.val == cur_node.val:
                    next_node = next_node.next
                if pre_node is None:
                    head = next_node
                else:
                    pre_node.next = next_node
            cur_node = next_node
        return head

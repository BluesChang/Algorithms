'''
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。例如，输入如下的链表1和链表2，则合并之后的升序链表如链表3所示。
链表1：1-->3-->5-->7
链表2：2-->4-->6-->8
链表3：1-->2-->3-->4-->5-->6-->7-->8
'''
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
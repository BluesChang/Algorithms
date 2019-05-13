'''
题目：输入两个链表，找出它们的第一个公共节点。
'''


class Solution:
    def find_first_common_node(self, headA, headB):
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

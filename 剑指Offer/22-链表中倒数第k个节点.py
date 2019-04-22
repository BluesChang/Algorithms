'''
题目：链表中倒数第k个节点
输入一个链表，输出该链表中倒数第K的结点，为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6，这个链表的倒数第3个节点是指为4的节点。
'''


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        if n == 0 or head is None:
            return None
        ahead_node = behind_node = head
        for i in range(n - 1):
            if ahead_node.next is not None:
                ahead_node = ahead_node.next
            else:
                return None
        while ahead_node.next is not None:
            ahead_node = ahead_node.next
            behind_node = behind_node.next
        return behind_node

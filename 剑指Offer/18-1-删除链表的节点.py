'''
题目：
在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def delete_node(self, head_node, to_be_deleted_node):
        if not isinstance(head_node, Node) or not isinstance(to_be_deleted_node, Node):
            return
        if to_be_deleted_node.next is not None:
            next_node = to_be_deleted_node.next
            to_be_deleted_node.val = next_node.val
            to_be_deleted_node.next = next_node.next
        elif head_node == to_be_deleted_node:
            head_node = None
        else:
            tmp = head_node
            while tmp.next != to_be_deleted_node:
                tmp = tmp.next
            tmp.next = None
        return head_node

    def show(self, head):
        while head is not None:
            print(head.val, end=' ')
            head = head.next
        print()


head = Node(1)
tmp = head
for i in range(2, 10):
    tmp.next = Node(i)
    tmp = tmp.next
head = Solution().delete_node(head, head.next.next)
Solution().show(head)

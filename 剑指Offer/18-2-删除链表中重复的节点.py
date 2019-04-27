'''
题目：
删除链表中重复的节点。
在一个排序的链表中，如何删除重复的节点？例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def delete_duplication(self, head_node):
        if not isinstance(head_node, Node):
            return
        if head_node is None:
            return
        current_node = head_node
        pre_node = None
        while current_node is not None:
            next_node = current_node.next
            if next_node is None or next_node.val != current_node.val:
                pre_node = current_node
            else:
                while next_node is not None and next_node.val == current_node.val:
                    next_node = next_node.next
                if pre_node is None:
                    head_node = next_node
                else:
                    pre_node.next = next_node
            current_node = next_node
        return head_node

    def show(self, head_node):
        while head_node is not None:
            print(head_node.val, end=' ')
            head_node = head_node.next
        print()

    def insert(self, vals):
        head_node = current_node = Node(vals[0])
        for i in range(1, len(vals)):
            current_node.next = Node(vals[i])
            current_node = current_node.next
        return head_node


head_node = None
Solution().show(head_node)
vals = [1, 2, 3, 3, 4, 4, 5]
head_node = Solution().insert(vals)
head_node = Solution().delete_duplication(head_node)
Solution().show(head_node)

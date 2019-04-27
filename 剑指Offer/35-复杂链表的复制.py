'''
题目：复制一个复杂链表。在复杂链表中，每个节点除了有一个指针指向下一个节点，还有一个指针指向链表中的任一节点或空节点。
'''


class Solution:
    def clone(self, head):
        if not head:
            return
        self.clone_nodes(head)
        self.connect_sibling_nodes(head)
        return self.reconnect_nodes(head)

    def clone_nodes(self, head):
        while head:
            cloned_node = head
            head, head.next = cloned_node.next, cloned_node

    def connect_sibling_nodes(self, head):
        while head:
            cloned_node = head.next
            if head.random:
                cloned_node.random = head.random.next
            head = cloned_node.next

    def reconnect_nodes(self, head):
        cloned_head = cloned_node = head.next
        head.next = cloned_node.next
        head = head.next
        while head:
            cloned_node.next = head.next
            cloned_node = cloned_node.next
            head.next = cloned_node.next
            head = head.next
        return cloned_head

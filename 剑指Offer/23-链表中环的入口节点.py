'''
题目：如果一个链表中包含环，如何找出环的入口节点？例如，在如图所示的链表中，环的入口节点是节点3
         ___________
        |           |
1-->2-->3-->4-->5-->6
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def entry_node_of_loop(self, head):
        if head is None or head.next is None:
            return None
        slow_node = head.next
        fast_node = head.next.next
        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None or fast_node.next.next is None:
                return None
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        slow_node = head
        while slow_node != fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next
        return fast_node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

print(Solution().entry_node_of_loop(node1).val)

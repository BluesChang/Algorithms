'''
题目：
删除链表中重复的节点。
在一个排序的链表中，如何删除重复的节点？例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def delete_duplication(self,head_node):
        if not isinstance(head_node,Node):
            return
        if head_node==None:
            return
        pre_node=None
        p_node=head_node
        while p_node!=None:
            next_node = p_node.next
            need_delete=False
            if next_node!=None and next_node.val==p_node.val:
                need_delete=True
            if not need_delete:
                pre_node=p_node
                p_node=p_node.next
            else:
                val = p_node.val
                to_be_delete_node = p_node
                while to_be_delete_node!=None and to_be_delete_node.val==val:
                    to_be_delete_node=to_be_delete_node.next
                if pre_node==None:
                    p_node=next_node
                    head_node=next_node
                else:
                    pre_node.next=next_node
                p_node=next_node
            return head_node

    def show(self,head):
            while head != None:
                print(head.val, end=' ')
                head = head.next
            print()

    def insert(self,vals):
            head = current = Node(vals[0])
            for i in range(1, len(vals)):
                current.next = Node(vals[i])
                current = current.next
            return head

# head = insert(vals)
head = None
Solution().show(head)
vals = [1, 2, 3, 3, 4, 4, 5]
head = Solution().insert(vals)
head = Solution().delete_duplication(head)
Solution().show(head)
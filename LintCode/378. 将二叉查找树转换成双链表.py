"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """

    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return None
        self.inorder = []
        self.inorder_traversal(root)
        for i in range(len(self.inorder) - 1):
            self.inorder[i].next = self.inorder[i + 1]
            self.inorder[i + 1].prev = self.inorder[i]
        return self.inorder[0]

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.inorder.append(DoublyListNode(root.val))
        self.inorder_traversal(root.right)

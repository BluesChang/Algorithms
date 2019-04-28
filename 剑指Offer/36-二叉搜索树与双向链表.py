'''
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


class Solution:

    def convert(self, root):
        # write your code here
        if not root:
            return None
        self.inorder = []
        self.inorder_traversal(root)
        for i in range(len(self.inorder) - 1):
            self.inorder[i].right = self.inorder[i + 1]
            self.inorder[i + 1].left = self.inorder[i]
        return self.inorder[0]

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.inorder.append(root)
        self.inorder_traversal(root.right)

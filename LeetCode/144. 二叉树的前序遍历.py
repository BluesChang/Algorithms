# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归版本
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.preorder_traversal(root)
        return self.res

    def preorder_traversal(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)


# 非递归版本
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        if root:
            stack.append(root)
            while len(stack) != 0:
                head = stack.pop()
                res.append(head.val)
                if head.right is not None:
                    stack.append(head.right)
                if head.left is not None:
                    stack.append(head.left)
        return res

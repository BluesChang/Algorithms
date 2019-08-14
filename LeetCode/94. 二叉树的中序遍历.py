# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归版本
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.inorder_traversal(root)
        return self.res

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.res.append(root.val)
        self.inorder_traversal(root.right)


# 非递归版本
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while len(stack) != 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

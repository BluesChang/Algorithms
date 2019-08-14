# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归版本
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.postorder_traversal(root)
        return self.res

    def postorder_traversal(self, root):
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        self.res.append(root.val)


# 非递归版本
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack1 = []
        stack2 = []
        if root:
            stack1.append(root)
            while stack1:
                head = stack1.pop()
                stack2.append(head.val)
                if head.left is not None:
                    stack1.append(head.left)
                if head.right is not None:
                    stack1.append(head.right)
            while stack2:
                res.append(stack2.pop())
        return res

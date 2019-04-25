'''
题目：从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
'''


class Solution:
    def print_from_top_to_bottom(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if root.left:
                queue.append(node.left)
            if root.right:
                queue.append(node.right)

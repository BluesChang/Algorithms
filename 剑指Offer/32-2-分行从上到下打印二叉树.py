'''
题目：从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
'''


class Solution:
    def print_from_top_to_bottom(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            next_queue = []
            result.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        print(result)

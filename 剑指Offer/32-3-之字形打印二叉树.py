'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二行按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此
类推。
'''
from collections import deque


class Solution:
    def print_from_top_to_bottom(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        is_from_left_to_right = True
        while queue:
            next_queue = []
            if is_from_left_to_right:
                result = [node.val for node in queue]
            else:
                result = [node.val for node in reversed(queue)]
            is_from_left_to_right = not is_from_left_to_right
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        print(result)

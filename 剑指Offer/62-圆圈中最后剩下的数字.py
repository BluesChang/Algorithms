'''
题目：0, 1, …, n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
'''

'''
方法一：经典的解法，用环形链表模拟圆圈
'''


class Node(object):
    def __init__(self, value, next=None):
        self.val = val
        self.next = next


class Solution:
    def last_remaining(self, n, m):
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            return
        next = None
        for i in range(n - 1, -1, -1):
            node = Node(value=i, next=next)
            if i == n - 1:
                last = node
            next = node
        head = next
        last.next = head
        current = head
        while id(current) != id(current.next):
            for _ in range(1, m):
                pre = current
                current = current.next
            pre.next = current.next
            current = pre.next
        return current.val


'''
方法二：创新的解法
'''


class Solution2:
    def last_remaining(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m % i)
        return last

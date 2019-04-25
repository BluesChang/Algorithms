'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列{1,2，3，4,5}是
某栈的压栈序列，序列{4,5,3,2,1}是该压栈序列对应的一个弹出序列，但{4,3,5,1,2}就不可能是该压栈序列的弹出序列。
'''


class Solution:
    def is_pop_order(self, p_push, p_pop):
        stack = []
        while p_pop:
            if p_push and p_push[0] == p_pop[0]:
                p_pop.pop()
                p_push.pop()
            elif stack and stack[-1] == p_pop[0]:
                stack.pop()
                p_pop.pop()
            elif p_push:
                stack.append(p_push.pop(0))
            else:
                return False
        return True

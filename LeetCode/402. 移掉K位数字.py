class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        if k == 0:
            return num
        stack = []
        for i in range(len(num)):
            while len(stack) != 0 and int(num[i]) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while len(stack) != 0 and k > 0:
            stack.pop()
            k -= 1
        res = ''.join(stack)
        if res == '':
            return '0'
        else:
            index = 0
            while res[index] == '0':
                if index == len(res) - 1:
                    return '0'
                index += 1
            return res[index:]

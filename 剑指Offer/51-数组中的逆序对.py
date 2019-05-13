'''
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组
中的逆序对的总数。例如，在数组{7,5,6,4}中，一共存在5个逆序对，分别是{7，6}、{7,5}、{7,4}、{6,4}和{5，4}。
'''


class Solution:
    def inverse_pairs(self, data):
        self.copy = [0] * len(data)
        return self.inverse_pairs_core(data, 0, len(data) - 1)

    def inverse_pairs_core(self, data, l, r):
        if l >= r:
            return 0
        middle = (l + r) >> 1
        result = self.inverse_pairs_core(data, l, middle) + self.inverse_pairs_core(data, middle + 1, r)
        i, j, k = l, middle + 1, l

        while i <= middle and j <= r:
            if data[i] > data[j]:
                self.copy[k] = data[j]
                j += 1
                result += middle - i + 1
            else:
                self.copy[k] = data[i]
                i += 1
            k += 1

        while i <= middle:
            self.copy[k] = data[i]
            i += 1
            k += 1

        while j <= r:
            self.copy[k] = data[j]
            j += 1
            k += 1
        for i in range(l, r + 1):
            data[i] = self.copy[i]

        return result

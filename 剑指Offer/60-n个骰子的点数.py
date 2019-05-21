'''
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
'''

'''
python式写法
'''


class Solution:
    def print_probability(self, num):
        probabilities = [[0 for i in range(6 * num + 1)] for i in range(num)]
        for i in range(6):
            probabilities[0][i] = 1
        for i in range(1, num):
            for j in range(i, 6 * (i + 1)):  # [0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
                probabilities[i][j] = probabilities[i - 1][j - 6] + probabilities[i - 1][j - 5] + probabilities[i - 1][
                    j - 4] + probabilities[i - 1][j - 3] + probabilities[i - 1][j - 2] + probabilities[i - 1][j - 1]
        result_probability = probabilities[num - 1]
        total = 6 ** num
        for s in range(num, 6 * num + 1):
            print(s, result_probability[s - 1] / total)


'''
书中方法
'''


class Solution2:
    max_value = 6

    def print_probability(self, num):
        if num < 1:
            return
        num_probability = num * self.max_value + 1
        probabilities1 = [0] * num_probability
        probabilities2 = [0] * num_probability
        for i in range(1, self.max_value + 1):
            probabilities1[i] = 1
        for k in range(2, num + 1):
            current_probabilities = probabilities1 if k % 2 == 1 else probabilities2
            last_probabilities = probabilities2 if k % 2 == 1 else probabilities1
            for i in range(1, k):
                current_probabilities[i] = 0
            for i in range(k, k * self.max_value + 1):
                current_probabilities[i] = 0

                for j in range(1, self.max_value + 1):
                    if j >= i:
                        break
                    current_probabilities[i] += last_probabilities[i - j]
        result_probability = probabilities1 if num % 2 == 1 else probabilities2
        total = self.max_value ** num
        for s in range(num, self.max_value * num + 1):
            print(s, result_probability[s] / total)

'''
题目：在一个mxn的期盼的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0。你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或向下移动一格，
直到到达棋盘的右下角。给定要给棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
'''


class Solution:
    def get_max_value(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0
        max_values = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = max_values[j]
                if j > 0:
                    left = max_values[j - 1]
                max_values[j] = max(up, left) + values[i * cols + j]
        max_value = max_values[cols - 1]
        return max_value


print(Solution().get_max_value([1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5], 4, 4))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        a1 = [0 for i in range(length)]
        a2 = [0 for i in range(length)]
        min_price = prices[0]
        for i in range(1, length):
            a1[i] = max(a1[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        max_price = prices[length - 1]
        for i in range(length - 2, -1, -1):
            a2[i] = max(a2[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])
        max_profit = 0
        for i in range(length):
            if a1[i] + a2[i] > max_profit:
                max_profit = a1[i] + a2[i]
        return max_profit

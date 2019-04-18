class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i - 1])
            result = result + h1 + h2 - height[i]
        return result - len(height) * h2

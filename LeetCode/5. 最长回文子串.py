class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = s[0]
        length = 1
        for r in range(1, len(s)):
            for l in range(r):
                if s[l] == s[r] and (l - r >= -2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_length = r - l + 1
                    if cur_length > length:
                        length = cur_length
                        res = s[l:r + 1]
        return res

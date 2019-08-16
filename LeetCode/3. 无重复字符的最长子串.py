class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        mapping = {}
        i = 0
        for j in range(len(s)):
            if s[j] in mapping:
                i = max(i, mapping[s[j]])
            ans = max(ans, j - i + 1)
            mapping[s[j]] = j + 1
        return ans

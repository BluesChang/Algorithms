class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
                i += 1
            else:
                j += 1
        return i

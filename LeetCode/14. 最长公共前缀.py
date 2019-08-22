class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = [len(set(i)) == 1 for i in zip(*strs)] + [0]
        return strs[0][:res.index(0)] if strs else ''

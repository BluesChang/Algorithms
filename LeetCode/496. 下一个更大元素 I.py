class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = dict()
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:
                hash_map[stack.pop()] = i
            stack.append(i)
        return [hash_map.get(i, -1) for i in nums1]

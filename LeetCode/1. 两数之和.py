class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return None
        keys = {}
        for k, v in enumerate(nums):
            if target - v in keys:
                return [keys[target - v], k]
            else:
                keys[v] = k
        return None

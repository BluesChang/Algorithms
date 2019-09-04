class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prevdiff = nums[1] - nums[0]
        count = 1 if prevdiff == 0 else 2
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (prevdiff >= 0 and diff < 0) or (prevdiff <= 0 and diff > 0):
                count += 1
                prevdiff = diff
        return count

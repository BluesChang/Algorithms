import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = sys.maxsize
        res = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    # print(i,l,r,diff,s)
                    res = s
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    return res
        return res

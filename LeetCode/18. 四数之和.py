class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l, r, target, n, cur_sum, res):
            if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
                return
            if n == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur_sum + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i - 1] != nums[i]):
                        findNsum(i + 1, r, target - nums[i], n - 1, cur_sum + [nums[i]], res)

        nums.sort()
        res = []
        findNsum(0, len(nums) - 1, target, 4, [], res)
        return res

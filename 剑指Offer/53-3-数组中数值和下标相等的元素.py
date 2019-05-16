'''
题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。
例如，在数组{-3，-1，1,3,5}中，数字3和它的下标相等。
'''


class Solution:
    def get_number_same_as_index(self, nums):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) >> 1
            if nums[mid] == mid:
                return mid
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1


print(Solution().get_number_same_as_index([-3, -1, 1, 3, 5]))

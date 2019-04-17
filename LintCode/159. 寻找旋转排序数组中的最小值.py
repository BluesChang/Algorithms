class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if not isinstance(nums, list):
            raise TypeError("Numbers is not a list!")
        if len(nums) == 0:
            raise ValueError("Numbers is empty!")
        index1 = 0
        index2 = len(nums) - 1
        index_mid = index1
        while nums[index1] >= nums[index2]:
            if index2 - index1 == 1:
                index_mid = index2
                break
            index_mid = (index1 + index2) // 2
            if nums[index1] == nums[index2] and nums[index1] == nums[index_mid]:
                result = nums[index1]
                for i in range(index1 + 1, len(nums)):
                    if result >= nums[i]:
                        result = nums[i]
                return result
            if nums[index_mid] >= nums[index1]:
                index1 = index_mid
            elif nums[index_mid] <= nums[index2]:
                index2 = index_mid
        return nums[index_mid]

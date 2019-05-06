class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return
        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)

    def partition(self, numbers, start, end, k):
        if start == end:
            return numbers[k]
        left, right = start, end
        pivot = numbers[(start + end) // 2]
        while left <= right:
            while left <= right and numbers[left] < pivot:
                left += 1
            while left <= right and numbers[right] > pivot:
                right -= 1
            if left <= right:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
                right -= 1
        if k <= right:
            return self.partition(numbers, start, right, k)
        if k >= left:
            return self.partition(numbers, left, end, k)
        return numbers[k]

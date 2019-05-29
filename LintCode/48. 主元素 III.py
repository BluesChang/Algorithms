class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """

    def majorityNumber(self, nums, k):
        # write your code here
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            elif len(counts) < k - 1:
                counts[num] = 1
            else:
                temps = []
                for count in counts:
                    counts[count] -= 1
                    if counts[count] == 0:
                        temps.append(count)
                for tmp in temps:
                    del counts[tmp]
        for count in counts:
            if nums.count(count) > len(nums) // k:
                return count

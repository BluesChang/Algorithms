class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """

    def majorityNumber(self, nums):
        # write your code here
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            elif len(counts) < 2:
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
            if nums.count(count) > len(nums) // 3:
                return count

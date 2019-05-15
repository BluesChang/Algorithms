class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end
        else:
            return [-1, -1]
        start = first
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            last = end
        else:
            last = start
        return [first, last]

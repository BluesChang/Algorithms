class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        # write your code here
        self.tmp = [0] * len(A)
        return self.mergeSort(A, 0, len(A) - 1)

    def mergeSort(self, A, l, r):
        if l >= r:
            return 0

        m = (l + r) >> 1
        ans = self.mergeSort(A, l, m) + self.mergeSort(A, m + 1, r)
        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if A[i] > A[j]:
                self.tmp[k] = A[j]
                j += 1
                ans += m - i + 1
            else:
                self.tmp[k] = A[i]
                i += 1
            k += 1

        while i <= m:
            self.tmp[k] = A[i]
            k += 1
            i += 1
        while j <= r:
            self.tmp[k] = A[j]
            k += 1
            j += 1
        for i in range(l, r + 1):
            A[i] = self.tmp[i]

        return ans

class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        # write your code here
        self.copy = [0] * len(A)
        return self.inverse_pairs_core(A, 0, len(A) - 1)

    def inverse_pairs_core(self, data, l, r):
        if l >= r:
            return 0

        middle = (l + r) >> 1
        result = self.inverse_pairs_core(data, l, middle) + self.inverse_pairs_core(data, middle + 1, r)
        i, j, k = l, middle + 1, l

        while i <= middle and j <= r:
            if data[i] > data[j]:
                self.copy[k] = data[j]
                j += 1
                result += middle - i + 1
            else:
                self.copy[k] = data[i]
                i += 1
            k += 1

        while i <= middle:
            self.copy[k] = data[i]
            i += 1
            k += 1

        while j <= r:
            self.copy[k] = data[j]
            j += 1
            k += 1
        for i in range(l, r + 1):
            data[i] = self.copy[i]

        return result

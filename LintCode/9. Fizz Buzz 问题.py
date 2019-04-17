class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_str = []
        for num in range(1, n + 1):
            if (num % 5 == 0) & (num % 3 == 0):
                list_str.append('fizz buzz')
            elif num % 5 == 0:
                list_str.append('buzz')
            elif num % 3 == 0:
                list_str.append('fizz')
            else:
                list_str.append(str(num))
        return list_str

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        -123
        -2147483648 - +2147483647
        """
        i = len(str(x)) - 1
        result = []
        while i >= 0:
            if i == 0 and str(x)[i] == '-':
                result = ['-'] + result
            else:
                result.append(str(x)[i])
            i -= 1
        num = int(''.join(result))
        return num if abs(num) < 2147483648 else 0
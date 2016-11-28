"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if (divisor == 0) or (divisor == -1 and dividend == MIN_INT):
            return MAX_INT

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        vals = []
        while dividend >= divisor:
            vals.insert(0, divisor)
            divisor += divisor
        res = 0
        for index, val in enumerate(vals):
            if dividend >= val:
                dividend -= val
                res += 2**(len(vals)-1-index)

        return sign*res

s = Solution()
print s.divide(19, 3)

import re
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        -123
        -2147483648 - +2147483647
        """
        compiled = re.compile(r"^(\-?)(\d*)$")
        operator, num = compiled.findall(str(x))[0]
        rev = int(''.join(num[::-1]))
        rev = 0 if abs(rev) < -2147483648 or abs(rev) > 2147483647 else rev
        return int(operator + str(rev))

s = Solution()
print s.reverse(-126000)
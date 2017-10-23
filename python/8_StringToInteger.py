"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""
import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        compiled = re.compile(r"^\s*[\+-]?\d+")
        m = compiled.search(str)
        if m:
            if int(m.group()) > 2147483647:
                return 2147483647
            elif -2147483648 > int(m.group()):
                return -2147483648
            else:
                return int(m.group())
        else:
            return 0
        


s = Solution()
print s.myAtoi("   +23.4")

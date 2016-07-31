"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

import re

class Solution(object):
    def __init__(self):
        self.number = re.compile(r"(\+?|\-?)(\d*\.?\d+$|\d+\.?\d*$|\d\.?\d*e\d+)")

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if self.number.match(s.strip()) else False


print Solution().isNumber("0")
print Solution().isNumber(" 0.1 ")
print Solution().isNumber("abc")
print Solution().isNumber("1 a")
print Solution().isNumber("2e10")
print Solution().isNumber(".1")
print Solution().isNumber(".")
print Solution().isNumber("3.")
print Solution().isNumber("-1.")

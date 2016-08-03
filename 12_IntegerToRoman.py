"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""
        for divider in [1000, 100, 10, 1]:
            num, letters = num % divider, num / divider
            if letters > 0:
                if letters < 4:
                    ans += numeral_map[divider]*letters
                elif letters % 5 == 4:
                    ans += numeral_map[divider] + numeral_map[divider * 5 * (letters / 5 + 1)]
                else:
                    ans += numeral_map[divider * 5] + numeral_map[divider] * (letters % 5)
        return ans


s = Solution()
print s.intToRoman(4)
print s.intToRoman(9)
print s.intToRoman(99)


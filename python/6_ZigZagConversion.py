"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = numRows
        r = 2*numRows - 2
        if r == 0:
            return s
        first = s[::r]
        last = s[n-1::r]
        mid = []
        for m in xrange(1, n-1):
            mid += [(s[r*x+m] if r*x+m < len(s) else "") + (s[r*(x+1)-m] if r*(x+1)-m < len(s) else "") for x in xrange(0, len(s)/r+1)]
        return first + "".join(mid) + last

s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("", 1)

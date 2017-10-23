"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        reverse(0, len(s)-1, s)
        p = 0
        for q, c in enumerate(s):
            if c == " ":
                reverse(p, q, s[p:q])
                p = q + 1
        return s





s = Solution()
print s.reverseWords("the sky is blue")

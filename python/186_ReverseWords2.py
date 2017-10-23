"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(self, string, start, end):
            while start < end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1
            return string
        reversed_s = self.reverse(s, 0, len(s) - 1)
        curr = 0
        next = 1
        while next < len(s):
            if reversed_s[next] == " ":
                break
            else:
                next += 1
        





s = "the sky is blue"
Solution().reverseWords(s)
print s

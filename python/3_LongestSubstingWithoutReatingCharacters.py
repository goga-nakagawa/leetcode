"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        indice = xrange(65, 123)

        i = 0
        for index, c in enumerate(s):
            i = max([indice[ord(c)], i])
            ans = max([ans, index - i + 1])
            indice[ord(c)] = index + 1

        return ans

s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("bbbbbb")
print s.lengthOfLongestSubstring("pwwkew")
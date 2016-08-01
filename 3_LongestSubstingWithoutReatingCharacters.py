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
        dup = set()
        ans, i, j = 0, 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in dup:
                dup.add(s[j])
                j += 1
                ans = max([ans, j - i])
            else:
                dup.remove(s[i])
                i += 1
        return ans



s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("bbbbbb")
print s.lengthOfLongestSubstring("pwwkew")
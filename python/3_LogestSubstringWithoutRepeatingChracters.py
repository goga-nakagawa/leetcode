"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from itertools import izip

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 1
        max_l = 1
        for curr, next in izip(s, s[1:]):
            if curr == next:
                cnt = 1
            else:
                cnt += 1
                max_l = max([max_l, cnt])
        return max_l


print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbbb")
print Solution().lengthOfLongestSubstring("pwwkew")
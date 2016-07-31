"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        p = 0
        q = len(s) - 1
        while p < q:
            while not s[p].isalnum() and p < q:
                p += 1
            while not s[q].isalnum() and p < q:
                q -= 1
            if s[p].lower() != s[q].lower():
                return False
            p += 1
            q -= 1

        return True





s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome(".,")

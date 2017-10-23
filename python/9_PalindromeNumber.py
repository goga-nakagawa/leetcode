"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        s = str(x)
        p = 0
        q = len(s) - 1
        while p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1
        return True

s = Solution()
print s.isPalindrome(123210)
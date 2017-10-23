"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

from collections import defaultdict
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = defaultdict(int)
        for i in xrange(n+1):
            if i < 3:
                dp[i] = i
            else:
                dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

s = Solution()
print s.climbStairs(6)